C=[(3,3,7,16),(3,9,12,21),(12,6,6,13),(12,7,12,19),(21,3,7,16),(21,9,12,21),(30,3,3,11),(30,9,10,18)]
for c in C:
 print(''.join(f"{x:02}"for x in c[2:]),end='')

##
import time
from cmath import *
g,r={},range
C=[7,16,12,21,5,14,11,20,7,16,12,21,3,11,10,18]
for i in r(8):
 for z in[3*exp(2j*pi*t/12)for t in r(*C[2*i:2*i+2])]:
  g={(round(z.real)+3+i//2*11,int(z.imag)+3+i%2*6):'2025'[i//2],**g}
  for y in r(13):
   print(''.join(g.get((x,y),' ')for x in r(40)))
  print();time.sleep(0.5)