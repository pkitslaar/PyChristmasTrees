chars = {
'2': ''
'xxxxx '
'x    x'
'    x '
'   x  '
' x    '
'xxxxxx'
,
'0': ''
' xxxx '
'x    x'
'x    x'
'x    x'
'x    x'
' xxxx '
,
'1':
'   xx '
'  x x '
' x  x '
'    x '
'    x '
' xxxxx'
,
'7':
'xxxxxx'
'    x '
'   x  '
'  x   '
'  x   '
'  x   '
}

W=6

def toHex(characters):
  hex_values = []
  for i in range(len(characters)//W):
	  row = characters[W*i:W*(i+1)]
	  bit_pattern = row.replace(' ', '0').replace('x', '1')
	  value = int(f'{bit_pattern}', 2)
	  c = chr(60+value)
	  #print(i, row, bit_pattern, value, chr(value), value+60, c)
	  hex_values.append(c)
  return ''.join(hex_values)

for k, characters in chars.items():
	hex_string = toHex(characters)
	print(k, hex_string)
