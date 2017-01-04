# Christmas Trees

[Back](README.md)

Vertical scrolling Christmas trees together with the greeting `~Merry Chirstmas~`. 
The trees are created with the characters from the greeting text.

Originally created to fit in a single tweet (max 140 characters): https://twitter.com/pkitslaar/status/812673564994371584

The code uses the [f-string](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings) syntax introduced in [Python](https://www.python.org/) 3.6.0.

## Code

```python
t='~Merry Christmas~'
b,s='|!'
for C in t:
 for (i,c) in enumerate(t+'||!'):
  print(f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}")
```

## Output

![Animated GIF of christmas.py console output](christmas.gif)

## Description

Below is a line-by-line description of the code.

### Line 1

> ```python
t='~Merry Christmas~'
```

Defines the main mesage of the script and will later also be used as the collection of characters used to draw the Christmas trees.

###Line 2

> ```python
b,s='|!'
```

Store the 'special' characters `'|'` and `'!'` as the variables `b` (from boom in Dutch) and `s` (don't know, maybe from special). Since we assing these to single letter variables we can use these instead of the literal character string. This saves 2 tokens per character. Furthermore, since the tuple unpacking notation is used we save another 3 characters with respect to standard assingment, like
```python
b='|'
s='!'
```

### Line 3

> ```python
> for C in t:
> ```
 
Outer loop. Each iteration here results in a new tree being output. 
The `C` (upper-case) character is the character used to fill the tree.

### Line 4

> ```python
>  for (i,c) in enumerate(t+'||!'):
> ```

Inner loop. Each iteration here produces a single line in the tree.

The enumerate yields a character `c` and the index (as an integer) of the character `i`.
The loops runs over the characters in `t` plus two `'|'` characters and a `'!'` character.

>> It can be seen that the brackets `(` and `)` are actually not needed for the tuple unpacking, so the code could be two characters shorter.

### Line 5

> ```python
>   print(f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}")
> ```

This is the main body of the script which contains the most logic.
The line contains a `print` function call with a single `f-string` as argument.
This string is the interesting part. 

```python
f"{ {s:t,b:b}.get(c,f'{c} {i*C} {c}'):^25}"
```

If we look at the various `{` and `}` characters we see there are a number of levels of expressions that are being evaluated.

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

The `get` method does a lookup in the dictionary and returns the corresponding value if found. If the key is not found in the dictionary the second argument of `get` is returned.

In this case the second argument is another `f-string`. Notice it is enclosed in single-quotes, since the outer `f-string`
is enclosed with double-quotes (`"`):

```python
f'{c} {i*C} {c}'
```

This code formats the actual lines of the tree. Inside there are two distinct expressions that are used

* `{c}`   : simply prints the current value of `c`
* `{i*C}` : Repeats (using the `*` operator) the value of `C` (upper-case) for `i` times.

Due to the two loops we get a new value for `C` (upper-case) for every tree, and a new value of `c` (lower-case) and `i` for every line in the tree.

Here are a few example results for this `f-string` for different values of `C`, `c` and `i`:

```
C  c  i  Line
-  -  -  ----
M  m  0  m  m
M  m  1  m M m
M  m  2  m MM m
M  m  3  m MMM m
~  e  5  e ~~~~~ e
```

So, looking back a the expression

```python
{s:t,b:b}.get(c,f'{c} {i*C} {c}')
```

We see this produces the following results

* If `c` == `'|'`, it will simply return `'|'` again. Which will become the trunk of the tree.
* If `c` == `'!'`, it will return the full text of `t`, so `'~Merry Christmas~`. Which is the closing mesage of each tree.
* In the other cases, the value of `c` will not be foud in the dictionary and the second argument to the `get` method is returned.

Finally, each of these results are centered inside a `25` character width string using the outer-most `f-string`.

