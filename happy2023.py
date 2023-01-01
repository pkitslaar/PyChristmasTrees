r,D,J,g=range,[4*"#","2,22, 2"," 3,33, 3",3*"0  0,"],20,{}
u=g.update
for b in"020010030010":
 x=int(b)
 l=D[x].split(',')[:3]
 for y in r(J):
  u({j:''for j in r(y+1)});u({y-j:f"{' '*(x%3)}{v}"for j,v in zip(r(4),l)})
  for y in r(20):print(g.get(y,''))
 J-=len(l)