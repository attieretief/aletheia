import subprocess, sys, json
from PIL import Image, ImageDraw, ImageFont
D="/Users/attieretief/Downloads/"
F="/System/Library/Fonts/HelveticaNeue.ttc"
def font(sz, bold=True): return ImageFont.truetype(F, sz, index=1 if bold else 0)
# title overlay
im=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
d.rectangle([0,1330,1080,1530],fill=(0,0,0,170))
t="“There’s no truth” isn’t true"; f=font(64)
w=d.textlength(t,font=f); d.text(((1080-w)/2,1395),t,font=f,fill="white"); im.save("title.png")
# end card
im=Image.new("RGB",(1080,1920),"black"); d=ImageDraw.Draw(im)
for txt,sz,y,col,b in [("Whose Truth?",70,820,"white",True),("the full essay at",44,930,(170,170,170),False),("aletheia.attieretief.com",58,1000,"white",True)]:
    f=font(sz,b); w=d.textlength(txt,font=f); d.text(((1080-w)/2,y),txt,font=f,fill=col)
im.save("end.png")

def build(segs, out, title_at):
    inputs=[]; fc=[]; n=0
    for src,a,b in segs:
        inputs+=["-ss",str(a),"-to",str(b),"-i",D+src]
        fc.append(f"[{n}:v]fps=30,crop=608:1080:626:0,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p[v{n}];[{n}:a]aresample=48000,afade=t=in:d=0.015,afade=t=out:st={b-a-0.02:.3f}:d=0.02[a{n}]")
        n+=1
    inputs+=["-loop","1","-t","3","-i","end.png","-f","lavfi","-t","3","-i","anullsrc=r=48000:cl=mono","-loop","1","-i","title.png"]
    fc.append(f"[{n}:v]fps=30,format=yuv420p,setsar=1[v{n}]"); fc.append(f"[{n+1}:a]aresample=48000[a{n}]")
    cat="".join(f"[v{i}][a{i}]" for i in range(n+1))
    fc.append(f"{cat}concat=n={n+1}:v=1:a=1[vc][ac]")
    fc.append(f"[vc][{n+2}:v]overlay=0:0:enable='between(t,{title_at},{title_at+3})':shortest=1[vo]")
    fc.append("[ac]loudnorm=I=-14:TP=-1.5:LRA=11[ao]")
    cmd=["ffmpeg","-v","error","-y",*inputs,"-filter_complex",";".join(fc),"-map","[vo]","-map","[ao]","-c:v","libx264","-preset","medium","-crf","19","-c:a","aac","-b:a","160k","-ar","48000","-movflags","+faststart",out]
    subprocess.run(cmd,check=True)
    print(out, subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],capture_output=True,text=True).stdout.strip())

segs=json.load(open(sys.argv[1])); build(segs["segs"], sys.argv[2], segs["title_at"])
