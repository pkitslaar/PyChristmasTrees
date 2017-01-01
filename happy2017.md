#Happy 2017

Prints `2017` in big fonts with varying fill characters.

Created as a tweet, so needed to fit in 140 characters: https://twitter.com/pkitslaar/status/815238499175538688

##Code

```python
for v in '~Xx*':
 print(''.join({'!':'\n'}.get(c,f'{ord(c)-60:06b}0') for c in '!zZB{!]]F>!>]N@!@]>D!L]>D!{Z[D').translate({48:32,49:v}))
```

##Output

![Animated GIF of happy2017.py console output](happy2017.gif)

##Description

The main part of this snippet revolves around the creation of the big 2017 characters. They are encoded in the large string enclosed in the generator expression on the second line.

The large string looks like this.

```python
 '!zZB{!]]F>!>]N@!@]>D!L]>D!{Z[D'
```

We will ignore the `!` in the string for now, they have a special meaning we will see later. We than find 6 chunks of 4 characters each.

```python
'zZB{'
']]F>'
'>]N@'
'@]>D'
'L]>D'
'{Z[D'
```

These codes are obtained from the (happy2017_fonts.py) script.

###font encoding

In the final script the goal is to create large characters to spell the year `2017`. Like

```
XXXXX   XXXX     XX  XXXXXX 
X    X X    X   X X      X  
    X  X    X  X  X     X   
   X   X    X     X    X    
 X     X    X     X    X    
XXXXXX  XXXX   XXXXX   X    
```

It would take too much space in the code snippet to spell out all the characters. The above text already occupies 175 characters/bytes. 

First, we isolate each digit and handle this. Let`s look at the `2`.
Here we also number the columns and rows in the grid.

```
  012345
  ------
0|XXXXX   
1|X    X  
2|    X   
3|   X    
4| X      
5|XXXXXX  
```

As can be seen the digit is made of a `6x6` grid. 
To encode this more efficiently we regard each row in the grid to be a bit pattern. 
Here tthe `X` represents a `1` and each ` ` (space) represents a `0`. 
So, each row represents an 6-bits number.

> **Intermezzo: Unicode and ASCII**
> In the digital world, all text characters are represented as integer values. 
> The most complete numbering system to represent characters is Unicode. 
> Each character in Unicode is represented by a code pointi, which simply is a number. 
> Almost every character in the world (real or fictional) as an Unicode code point value. 
> However, for our purpose we will only use very low numbers below 128. 
> In this range the Unicode code points map to the old ASCII system.
> 
> In Python the conversion between characters and their numeric value is done using the `chr` and `ord` built-in functions. 
> Below, are the help texts for `chr` and `ord`.
> 
> ```
> chr(i, /)
>     Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
> 
> ord(c, /)
>     Return the Unicode code point for a one-character string.
> ```

Based on this knowledge, we can lookup the ASCII character that is represented by the value of the bit patters in each row. 
However,  all numbers below 32 are non-printable characters which cannot be copy-pasted into a text box.
Therefore, we add `60` to the original bit-pattern value to get characters in the range of values that can be printed. 
Since the maximum value for a 6-bits integer is 63 we will never get above the 127, the end of the ASCII table.

The schematic below shows the bits and the corresponding value for the rows in the `2` figure. 
Also the original ASCII character and the value and character of the value plus 60 are shown.

```
  012345 bits   value  c    +60  c+60
  ------ -----  -----  -    ---  ----
0 xxxxx  111110 62     >    122  'z'
1 x    x 100001 33     !    93   ']'
2     x  000010 2      SOH  62   '>'
3    x   000100 4      EOT  64   '@'
4  x     010000 16     DLE  76   'L'
5 xxxxxx 111111 63     ?    123  '{'
```

Based on this, we can interpret the output of the `happy2017_fonts.py` script.

```bash
$ python happy2017_fonts.py
2 z]>@L{
0 Z]]]]Z
1 BFN>>[
7 {>@DDD
```

