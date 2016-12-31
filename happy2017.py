for v in '@#X%x&*':
 print(''.join({'!':'\n'}.get(c,f'{ord(c)-60:06b}0') for c in 'zZB{!]]F>!>]N@!@]>D!L]>D!{Z[D').translate({48:32,49:v}))
