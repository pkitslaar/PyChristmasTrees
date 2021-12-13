n,P={},lambda H,W,h=0,w=0:[(h+i//W,w+i%W)for i in range(W*H)]
g=dict(zip(P(3,3,9,10),map(int,f'{191:b}')));G=lambda x:g.get(x,0)
while 1:
 for p in P(20,40):y,x=p;V,S=G(p),sum(map(G,P(3,3,y-1,x-1)));n[p]=(V&(S in(3,4)))|((not V)&(S==3));print('.*'[n[p]],end='\n'*(x==39))
 g={**n}