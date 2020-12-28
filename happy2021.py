two = """\
11111111#
11111111#
      11#
11111111#
11111111#
11      #
11111111#
11111111#"""

two_small = """\
11111#
   11#
11111#
11   #
11111#"""

zero="""\
  1111  #
111  111#
111  111#
111  111#
111  111#
111  111#
111  111#
  1111  #"""

zero_small = """\
 111 #
1   1#
1   1#
1   1#
 111 #"""

vacine="""\
   11   #
  1  1  #
  1111  #
  1  1  #
  1  1  #
11111111#
   11   #
  1111  #"""

vacine_small="""\
  1  #
 1 1 #
 1 1 #
11111#
  1  #"""

def ascii_to_int_columns(ascii_txt, num_rows=8, num_cols=0):
    if not num_cols:
      num_cols = num_rows
    grid = [list(row[:num_cols]) for row in ascii_txt.splitlines()]
    grid_T = [[' ']*num_rows for _ in range(num_cols)]
    for y in range(num_rows):
        for x in range(num_cols):
            grid_T[x][y]=grid[y][x]
    return [int(f"0b{''.join(row)}".replace(' ','0'),2) for row in grid_T]

two_columns = ascii_to_int_columns(two)
two_small_columns = ascii_to_int_columns(two_small,5)

zero_columns = ascii_to_int_columns(zero)
zero_columns_small = ascii_to_int_columns(zero_small, 5)

vacince_columns = ascii_to_int_columns(vacine)
vacince_columns_small = ascii_to_int_columns(vacine_small, 5)

zero_and_vacine = zero_small + '\n' + vacine_small
print(zero_and_vacine)
zero_and_vacine_columns = ascii_to_int_columns(zero_and_vacine, 10,5)
print(zero_and_vacine_columns)
for i in range(10):
  print(*[f'{c:0>10b}'[i].replace('0',' ') for c in zero_and_vacine_columns],sep='')
#1/0
for i in zero_and_vacine_columns:
  print(f'{i:0>10b}', f'{i:x}')
separator = [0]*2

def toHex(int_list):
  return ''.join(f'{i:0>2x}' for i in int_list)

print('two', toHex(two_columns))
print('two_small', toHex(two_small_columns))
print('zero', toHex(zero_columns))
print('zero_small', toHex(zero_columns_small))

print('vacine', toHex(vacince_columns))
print('vacine_small', toHex(vacince_columns_small))

print('zero+vacine_small', toHex(zero_and_vacine_columns))
T,Z,X,V='1717151d1d','0e'+6*'1'+'0e','0'*4,[450,558,563,558,450]
r,D=range,T+X+Z+X+T+X
C=[(i,int(f'{D[i:i+2]}',16))for i in r(0,42,2)]+[(80,i) for i in V]
for t in r(185):
 i,k=t//6,t%5
 print('\n'[k:],*[f"{c>>max(5+(j//14*5)-i,0):>10b}"[5+k].replace('0',' ')for j,c in C],sep='')