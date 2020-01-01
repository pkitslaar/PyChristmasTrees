g=[[' ']*30 for i in range(12)]
b,y,x='9ccc999aaa999ccc122221222208cc4888880aaa299999202291aa88888822aaaa999999ccc888aa',10,7
for h in b:
 v=int(h,16)
 y+={0:1,1:-1}.get(v&7,0)
 x+={2:1,4:-1}.get(v&7,0)
 g[y][x]='.#'[v>>3]
 [print(*r,sep='') for r in g]