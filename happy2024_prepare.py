"""
Code to generate the hex representation of the bye2021.py number grid
"""

grid_2024="""\
  ##     #    ##   #  #
    #  #  #     #  #  #
  ##   #  #   ##    ## 
 #     #  #  #        #
  ##    ##    ##      #
"""

def parse(txt):
    grid={}
    for y,line in enumerate(txt.splitlines()):
        for x,v in enumerate(line):
            if v!=' ':
                grid[(y,x)]=1
    #
    y_locations = [p[0] for p in grid]
    min_y, max_y = min(y_locations), max(y_locations)
    print(min_y, max_y)

    #
    x_locations = [p[1] for p in grid]
    min_x, max_x = min(x_locations), max(x_locations)
    print(min_x, max_x)

    combined_string = ''
    for y in range(min_y, max_y+1):
        bits = []
        for x in range(min_x, max_x+1):
            bits.append(str(grid.get((y,x),0)))
        bits_string = ''.join(bits)
        combined_string += bits_string
        bits_int = int(bits_string,2)
        print(bits_string, len(bits_string),bits_int, hex(bits_int))
    combined_int = int(combined_string,2)
    print(len(combined_string))
    print(combined_string, combined_int)
    print(hex(combined_int))
    return hex(combined_int), max_x-min_x+1

code, w = parse(grid_2024)
bit_pattern = f'0{int(code,16):b}'
print(len(bit_pattern))
for i in range(0,len(bit_pattern),w):
    print(bit_pattern[i:i+w].replace('0',' ').replace('1','#'))
