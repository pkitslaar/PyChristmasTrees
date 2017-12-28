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

The first 4 lines of the code deal with the setup of the variables and the main data storage
dictionary `l`. This dictionary is the actual staff that gets printed in the last line of the code.

### Line 1

```python
H,b='FEDCBAgfed','|'
```

The first line defines two variables `H` and `b`.  
Here `H` defines the note names of the positions on the staff from high to low. Here captial letters are used to define the notes an octave above the lower case note names. 
The `b` variable is used to keep a reference to the `'|'` character, which is used to indicate end of
a bar in the staff.

Next, we will first discuss line 4, which holds the actual staff data that will be printed.

### Line 4

```python
l={c:[k]*64 for k,c in zip('- '*5,H)}
```

The variable `l` is a dictionary with keys the note names on the staff and with values a
list of characters for each line.

Here dictionary comprehension is used to define the dictionary. The code
```python
{c:[k]*64 for ...}
``` 
reads as. Create a dictionary with a key from variable `c` and values `[k]*64`.
This last part creates a list with 64 copies of the value `k`.

The end part of the dictionary comprehension defines the values for `k` and `c`.
```python
{... for k,c in zip('- '*5,H)}
```
Here the `k,c` unpacks to tuples returned by the `zip` expression.
The zip expression combines the values from the two sequences and returns pairs for each side.

The first sequence is a character string with alternating `'-'` and `' '` characters, repeated 5 times.
So this could also be written as `'- - - - - '` but that would take 4 characters more.

The second sequence are the names of the note positions defined in `H`.

The alternating `k` values, make sure that there will be lines and spaces in note staff.

The final content of `l` after the execution of this line will look like.

```
{
'F': '----------------------------------------------------------------',
'E': '                                                                ',
'D': '----------------------------------------------------------------',
'C': '                                                                ',
'B': '----------------------------------------------------------------',
'A': '                                                                ',
'g': '----------------------------------------------------------------',
'f': '                                                                ',
'e': '----------------------------------------------------------------',
'd': '                                                                ',
}
