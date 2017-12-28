# Christmas 2017

[Back](README.md)

Prints `We whish you a merry Chirstmas!` notes.

Created as a [tweet](https://twitter.com/pkitslaar/status/945222840210649088). Since Twitter decided to increase the
length of tweets to be 280 characters that is the size of the code.

## Code

```python
H,b='FEDCBAgfed','|'
n='&g#F3D/D4Dd|4g8gAgf|4eee|4A8ABAg|4fdd|4B8BCBA|4ge8dd|4eAf|2g'.replace(b,'|ECAf d')
i,I=2,iter(n)
l={c:[k]*64 for k,c in zip('- '*5,H)}
for x in I:
 if not x in H:
  c,x=x,next(I)
 l[x][i]=c
 i+={'4':2,b:0}.get(c,1)
 print(*map(''.join,l.values()),sep="\n")
```

## Output

![Animated GIF of christmas2017.py console output](christmas2017.gif)

## Description

blah..
