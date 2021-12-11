import time
import itertools
r,P=range,itertools.product
glider = [8,4,28,0,0,0,0,0]

# .1. = 2
# 111 = 7
# 111 = 7

N,a=(-1,2),'1'
g=[[*f'{(2**14)*b+(2**5)*b:040b}']for b in [0,0,0,0,0,0,0,0,0,2,7,7,0,0,0,0,0,0,0,0]]
n=[i[:]for i in g];n[0][0]='1'
while n!=g:
 [print(''.join(r))for r in g]
 for y,x in P(r(20),r(40)): 
  z,S=g[y][x]==a,sum(g[(y+v)%19][(x+u)%39]==a for v,u in P(r(*N),r(*N)))
  n[y][x]='.1'[(z and S in(3,4))or(not z and S==3)]
 g,n=n,g
 print()
 time.sleep(0.1)
