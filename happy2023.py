"""
2222
   *
   *
  **
####
*
*
**
2222
0000
#  #
#  #
#  #
#  #
0000
2222
   *
   *
  ** 
####
*
*
**
2222
3333 
   *
  **
   *    
3333
"""
import time
I=0
r,D,J=range,dict(zip("HVLlT",[4*"#",4*"*,","*,*,**"," *, *,**"," *,**, *"])),32
g={y:''for y in r(J)}
u=g.update
for b in"HTHHLHlHHVHHLHlH":
 for y in r(J):
  u({j:''for j in r(y+1)});u({y-j:v for j,v in enumerate(D[b].split(','))})
  for y in r(32):print(g[y])
 J=min(p for p,v in g.items()if v and p>-1)