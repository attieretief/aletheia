"""Jump-cut by word timestamps: any gap between consecutive words longer than MIN_GAP inside a
segment is shrunk to AFTER s of air after the word plus BEFORE s before the next one.
Whisper words longer than LONG s hide a pause; those are split at their quietest stretch."""
import json, sys, wave, struct, math
MIN_GAP=0.30; AFTER=0.08; BEFORE=0.12; HOLD_KEEP=0.7; LONG=0.9; FR=0.02
def env(src):
    w=wave.open(src.replace(".mp4",".wav")); sr=w.getframerate(); n=w.getnframes()
    d=struct.unpack(f"<{n}h",w.readframes(n)); k=int(sr*FR)
    return [20*math.log10(max(1,math.sqrt(sum(x*x for x in d[i:i+k])/k))/32768) for i in range(0,n-k,k)]
cfg=json.load(open(sys.argv[1])); hold=cfg.get("hold",[]); out=[]; C={}
for src,a,b in cfg["segs"]:
    if src not in C:
        d=json.load(open(src.replace(".mp4",".json"))); C[src]=([(w["start"],w["end"]) for s in d["segments"] for w in s["words"]],env(src))
    ws,e=C[src]; ws=[w for w in ws if w[0]>=a-0.05 and w[1]<=b+0.05]
    # split long words: find longest run below (min+8dB) inside, treat as gap
    spans=[]
    for s0,e0 in ws:
        if e0-s0>LONG:
            fr=e[int(s0/FR):int(e0/FR)]; lo=min(fr)+8; best=(0,0,0); st=None
            for i,v in enumerate(fr+[999]):
                if v<lo and st is None: st=i
                if v>=lo and st is not None:
                    if i-st>best[0]: best=(i-st,st,i)
                    st=None
            if best[0]*FR>MIN_GAP:
                spans+= [(s0,s0+best[1]*FR),(s0+best[2]*FR,e0)]; continue
        spans.append((s0,e0))
    cur=a; pieces=[]
    for (s0,e0),(s1,e1) in zip(spans,spans[1:]):
        gap=s1-e0
        if gap<=MIN_GAP: continue
        keep=HOLD_KEEP if any(h[0]==src and e0-0.3<=h[1]<=s1+0.3 for h in hold) else AFTER+BEFORE
        if gap<=keep: continue
        c0=e0+keep*AFTER/(AFTER+BEFORE); c1=s1-keep*BEFORE/(AFTER+BEFORE)
        pieces.append([src,round(cur,3),round(c0,3)]); cur=c1
    pieces.append([src,round(cur,3),b]); out.append(pieces)
t=sum(p[2]-p[1] for seg in out[:cfg["title_seg"]] for p in seg)
flat=[p for seg in out for p in seg]
json.dump({"title_at":round(t,2),"segs":flat},open(sys.argv[2],"w"))
print(sys.argv[2],len(flat),"pieces","%.1fs"%sum(p[2]-p[1] for p in flat),"title_at %.2f"%t)
