w,D,r=29,{'a':63,'b':33,'c':1,'d':32,48:32},range
for X in r(w*2):
 x=X%w;s,e,c=((x,None,'<'),(0,x,'>'))[X<w]
 print('\n'.join("{1:{0}29}".format(c,''.join(R[s:e])).translate(D) for R in 
 [' '.join([f"{D[p]:06b}" for p in 'aabbcbabdbbbaa'[k:k+2]*2]) for k in r(0,14,2)]))
