import json,os,sys,urllib.request as u,random,lzma,base64
E=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no env")
exec(lzma.decompress(base64.b64decode("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")))
def p(a,o):
 q=u.Request(E+a,data=json.dumps(o).encode(),headers={"content-type":"application/json"})
 with u.urlopen(q) as s:return json.load(s)
def U_(x):
 f=(ord(x[1])-49)*16+ord(x[0])-97
 t=(ord(x[3])-49)*16+ord(x[2])-97
 m=f|t<<7
 if len(x)==5:m|=("nbrq".index(x[4])+2)<<14
 return m
while 1:
 gm=p("/game",{})
 if gm["status"]=="done":break
 while gm["status"]=="your_move":
  F(gm["fen"])
  ms=[(x,U_(x)) for x in gm["legal_moves"]]
  if len(ms)==1:mv=ms[0][0]
  else:
   _,bm=Rt([m for _,m in ms])
   mv=[x for x,m in ms if m==bm][0]
  gm=p("/move",{"game":gm["game"],"move":mv})
