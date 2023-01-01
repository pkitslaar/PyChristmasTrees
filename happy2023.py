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
#HVLlT
#01234
r,D,J,g=range,[4*"#",4*"*,","*,*,**"," *, *,**"," *,**, *"],32,{}
u=g.update
for b in"0400203001002030":
 l=D[int(b)].split(',')[:4]
 for y in r(J):
  u({j:''for j in r(y+1)});u({y-j:v for j,v in zip(r(4),l)})
 for y in r(32):print(g.get(y,''))
 J-=len(l)