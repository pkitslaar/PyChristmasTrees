two_small = """\
11111#
   11#
11111#
11   #
11111#"""

zero_small = """\
 111 #
1   1#
1   1#
1   1#
 111 #"""

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

two_small_columns = ascii_to_int_columns(two_small,5)
zero_columns_small = ascii_to_int_columns(zero_small, 5)
zero_and_vacine = zero_small + '\n' + vacine_small
zero_and_vacine_columns = ascii_to_int_columns(zero_and_vacine, 10,5)

print('two_small[int]', two_small_columns)
print('zero_small[int]', zero_columns_small)
print('zero+vacine_small[int]', zero_and_vacine_columns)

[print(['',f'{"inject 2021":>{36-t//5}}'[:24]+'\n'][t%5==0],
*[f' {"2020|"[(t-5)//25]}'[int(f"{c>>max(5+(j//6*5)-t//5,0):0>10b}"[5+t%5])]for j,c in [
(i+6*(i>17),(0,23,21,29,14,17,450,558,563)[int(j)])for i,j in enumerate(
'112330455540112330678760')]],sep='')for t in range(130)]