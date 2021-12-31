n,P={},lambda w,h,H=5,W=15:[(h+i//W,w+i%W)for i in range(W*H)]
g,G=dict(zip(P(9,2),f'{0x77762a25d5ca2a17777:b}')),lambda x:int(g.get(x,0))
while 1:
 for p in P(0,0,9,32):y,x=p;V,S=G(p),sum(map(G,P(x-1,y-1,3,3)));n[p]=V&(2<S<5)|(V^1)&(S==3);print(' *'[V],end='\n'[31-x:])
 g={**n}