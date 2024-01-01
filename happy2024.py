W,r=22,range
N=(0,0),(0,1),(-1,1),(1,1)
s,S=' *'
g={(1+i%W,3+i//W):'#'for i,v in enumerate(f'0{0x1821891241258918682480586181:b}')if v=='1'}
for i in r(370):
 n={((i**3)%(W+2),0):S}
 for(x,y),c in g.items():
  O=N[0]
  match[g.get((x+X,y+Y),s)for X,Y in N]:
   case'*',' ',_,_:O=N[1]
   case'*',d,' ',_ if d!=s:O=N[2]
   case'*',d,_,' ' if d!=s:O=N[3]
  x+=O[0];y+=O[1]
  n[x,y]=c if (y<10 and x>-1 and x<W+2) else '^'
 g=n
 for H in r(12):
  print(''.join(g.get((x,H),s)for x in r(-2,W+4)))
 import time;time.sleep(0.1)