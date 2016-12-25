#christmas

A vertical scrolling Christmas trees with the text *Merry Chirstmas*.

Originally created as a tweet at: https://twitter.com/pkitslaar/status/812673564994371584

The code uses the `f-string` syntax introduced in Python 3.6.0.

##Code

```python
t='~Merry Christmas~'
b,s='|!'
for C in t:
 for (i,c) in enumerate(t+'||!'):
  print(f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}")
```

##Output

![Animated GIF of christmas.py console output](christmas.gif)

##Description

> ```python
t='~Merry Christmas~'
```

Define the text string with the message and the collection of characters used to fill the chirstmas trees.

> ```python
b,s='|!'
```

Store the 'special' characters `|` and `!` as the variables `b` and `s`.
Shorter notation than
```python
b = '|'
s = '!'
```

> ```python
for C in t:
```

Outer loop. Each iteration here results in a new tree being output. 
The `C` character is the character used to fill the tree.

> ```python
 for (i,c) in enumerate(t+'||!'):
```

Inner loop. Which produces all the lines in the tree.
Loops over the characters in `t` plus an additional number of `|` and `!` characters.
These have special meaning as can be seen in the next section.

* `i` : line number of the tree
* `c` : current character from the text

> ```python
  print(f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}")
```

This is the main body of the script which contains the most logic.
The line contains a `print` function call with a single `f-string` as argument.
This string is the interesting part. 

```python
f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}"
```

If we look at the `{` and `}` characted we see there are a number of levels of expressions that are being evaluated.

At the outermost level we can look at the string as

```python
f"{ ... :^25}"
```

Which simply takes the results of the expression at the location of `...` and produces a centered string (`^`) of length `25` padded with spaces.

At the next level we look at the expression denoted `...` above

```python
{s:t,b:b}.get(c,f'{c} {i*C} {c}')
```

Looking at the left side of the `.` we find a (literal) dictionary construction

```python
{s:t,b:b}
```

Here we find the references to the `s` and `b` variables we defined at the start.

The dictionary contains two entries. 

* `b:b` => So, with the key `'|'` (value of `b`) and also the value `'!'` (again value of `b`).
* `s:t` => Here the key is `'!'` (value of `s`) and the value is `'~Merry Chistmas~'` (the value of `t`)

So this is equivalant to

```python
{
 '|' : '|',
 '!' : '~Merry Christmas~'
}
```

Due to the earlier definitions of the `b` and `s` this saves a lot of characters, even when creating a simple single character keys/values.

Next, we look at the right side of the `.`

```python
{...}.get(c,f'{c} {i*C} {c}')
```

Here we call the `get` method on the dictionary with as first argument the value of `c`, so the current character from the inner loop.

The `get` method does a lookup in the dictionary and returns the corresponding value if found. The the key is not found in the dictionary the second argument of `get` is returned.

In this case the second argument is another f-string:

```python
f'{c} {i*C} {c}'
```

This code formats the actual lines of the tree. Inside ther are 2 distinct expressions that are used

* `{c}`   : simply prints the current value of `c`
* `{i*C}` : Repeats (using the `*` operator) the value of `C` (note capital) for `i` times.

Due to the two loops we get a new value for `C` (upper-case) for every tree, and a new value of `c` (lower-case) and `i` for every line in the tree.

Here are a few example lines for different value of `C`, `c` and `i`.

```
C  c  i  Line
-  -  -  ---------------------
M  m  0  m  m
M  m  1  m M m
M  m  2  m MM m
M  m  3  m MMM m
~  e  5  e ~~~~~ e
```

So, looking back a the line

```python
{s:t,b:b}.get(c,f'{c} {i*C} {c}')
```

We see this produces the following results

* If `c` == `|`, it will simply return `|` again. Which will become the trunk of the tree.
* If `c` == `!`, it will return the full text of `t`, so `'~Merry Christmas~`. Which is the closing mesage of each tree.
* In the other cases, the value of `c` is not in the dictionary and the second argument to `get` is returned.

Finally, this result is centered to `25` characters using the outer-most f-string.

