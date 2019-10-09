import binascii as B
g=[[' ']*30 for i in range(12)]
b,y,x=B.a2b_base64('nMyZmqqZnMwSIiEiIgjMSIiICqopmZkgIpGqiIiIIqqqmZmZzMiIqg==').hex(),10,7
for h in b:
 v=int(h,16)
 y+={0:1,1:-1}.get(v&7,0)
 x+={2:1,4:-1}.get(v&7,0)
 g[y][x]='.#'[v>>3]
 [print(*r,sep='') for r in g]
