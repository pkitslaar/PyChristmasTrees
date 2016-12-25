t='~Merry Christmas~'
b,s='|!'
for C in t:
 for (i,c) in enumerate(t+'||!'):
  print(f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}")
