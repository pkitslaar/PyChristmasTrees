import time
from cmath import *
W,H,r=40,13,range;g=[' ']*H*W
C=[7,16,12,21,5,14,11,20,7,16,12,21,3,11,10,18]
for i in r(8):
 for z in[3*exp(2j*pi*t/12)for t in r(*C[2*i:2*i+2])]:
  g[(round(z.real)+3+i//2*11)+W*(int(z.imag)+3+i%2*6)]='2025'[i//2]
  [print(*g[y*W:][:W],sep='')for y in r(H)];print()
  time.sleep(0.5)