##christmas

A vertical scrolling Christmas trees with the text *Merry Chirstmas*.

Originally created as a tweet at: https://twitter.com/pkitslaar/status/812673564994371584

The code uses the `f-string` syntax introduced in Python 3.6.0.

Code:

```python
t='~Merry Christmas~'
b,s='|!'
for C in t:
 for (i,c) in enumerate(t+'||!'):
  print(f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}")
```

Output:

![Animated GIF of christmas.py console output](christmas.gif)
