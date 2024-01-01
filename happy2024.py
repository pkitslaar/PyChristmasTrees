W,r=22,range
N=(0,0),(0,1),(-1,1),(1,1)
s,S=' *'
g={(1+i%W,3+i//W):'#'for i,v in enumerate(f'0{0x1821891241258918682480586181:b}')if v=='1'}
for i in r(242):
 n,G={(i**3%(W+2),0):S},g.get
 for x,y in g:
  I,m=0,[G((x+X,y+Y),s)for X,Y in N]
  match m:
   case'*',' ',_,_:I=1
   case'*',d,' ',_ if d!=s:I=2*(x>-3)
   case'*',d,_,' ' if d!=s:I=3*(x<W+1)
  n[x+N[I][0],min([y+N[I][1],9])]=m[0]
 for H in r(1,11):
  print(''.join(G((x,H),s).replace('#','█ '[i<241])for x in r(-1,W+4)))
 g=n
 import time;time.sleep(0.05)