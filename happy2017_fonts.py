"""
Script to encode binary ASCII-art drawings into
printable character string.

Used for the create happy2017.py snippet, originally
tweeted at: https://twitter.com/pkitslaar/status/815238499175538688

See also: https://github.com/pkitslaar/PyChristmasTrees

"""

# Collection of characters with drawings
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

# Width of the drawing
W=6

def encode(characters, verbose=False):
  """Outputs a encode version of the input drawing (characters)"""
  encoded_values = []
  for i in range(len(characters)//W):
    row = characters[W*i:W*(i+1)]
    bit_pattern = row.replace(' ', '0').replace('x', '1')
    value = int(f'{bit_pattern}', 2)
    c = chr(60+value)
    if verbose:
      print(i, row, bit_pattern, value, chr(value), value+60, c)
    encoded_values.append(c)
  return ''.join(encoded_values)

def main(args):
  for k, characters in chars.items():
    encoded_string = encode(characters, args.verbose)
    print(k, encoded_string)

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser('Create encoded big fonts')
  parser.add_argument('-v', '--verbose',dest='verbose', action='store_true')
  args = parser.parse_args()
  main(args)
