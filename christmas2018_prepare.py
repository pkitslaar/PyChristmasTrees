import numpy as np
import scipy.ndimage
import time

class GridCoords(object):
    """Helper class to easily handle coordinates in a 2D numpy array (grid)"""

    def __init__(self, grid_shape, grid_indices = None):
        self.grid_shape = grid_shape
        self.grid_indices = grid_indices or (np.empty(0), np.empty(0))

    def Y(self):
        return self.grid_indices[0]
    
    def X(self):
        return self.grid_indices[1]

    def as_tuples(self):
        return zip(*self.grid_indices)

    def __str__(self):
        return str(list(self.as_tuples()))

    def filter(self, include):
        return GridCoords(self.grid_shape, 
            (
                self.grid_indices[0][include],
                self.grid_indices[1][include],
            ))

    def get_values(self, value_map):
        return value_map[self.grid_indices]

    @staticmethod
    def combine(*grid_coords):
        combined_y = np.hstack([gc.Y() for gc in grid_coords])
        combined_x = np.hstack([gc.X() for gc in grid_coords])
        first_shape = grid_coords[0].grid_shape
        assert(all(first_shape == gc.grid_shape for gc in grid_coords))
        return GridCoords(first_shape, (combined_y, combined_x))

    @staticmethod
    def neighborhood(shape, center_y, center_x):
        offsets = [
            (-1, 0),
            ( 1, 0),
            ( 0, 1),
            ( 0,-1)
        ]
        neighbours_y = [] 
        neighbours_x = [] 
        for offset_x, offset_y in offsets:
            if 0 <= center_x+offset_x < shape[1] and 0 <= center_y+offset_y < shape[0]:
                neighbours_y.append(center_y+offset_y)
                neighbours_x.append(center_x+offset_x)
        return GridCoords(shape, (np.array(neighbours_y), np.array(neighbours_x)))
bmp = scipy.ndimage.imread('christmas2018_text3.bmp', mode='P').astype(np.int)
CHAR_TABLE = {225: ' ', 182: '-', 139: '?', 0: '#'}

def print_grid(g, table = CHAR_TABLE):
    for r in g:
        print(''.join([table[v] for v in r]))
print_grid(bmp)


visisted = np.zeros_like(bmp)
#next_pos = (15,1)
next_pos = (10,7)
positions = [next_pos]
while next_pos:
    next_pos = None
    c_pos = positions[-1]
    y, x= c_pos
    current = bmp[y][x]
    visisted[y][x] = 1 if current == 0 else 2

    nh = GridCoords.neighborhood(bmp.shape, y,x)
    in_bmp = nh.get_values(bmp) < 225 
    not_visited = nh.get_values(visisted) == 0
    next_options = in_bmp & not_visited
    if np.any(next_options):
        option_coords = nh.filter(next_options)
        option_values = option_coords.get_values(bmp)
        combined = list(zip(option_values, option_coords.as_tuples()))
        combined.sort(reverse = False)
        next_pos = combined[0][1]
        positions.append(next_pos)
        print_grid(visisted, {0: ' ', 1: '#', 2: '-'})
        print()
        time.sleep(0.1)
print(positions)
prev_p = positions[0]
delta_to_bits = {
     1+0J:int('0000', 2),
    -1+0J:int('0001', 2),
       1J:int('0010', 2),
      -1J:int('0100', 2),}

all_bits = []
for next_p in positions[1:]:
    y, x= next_p
    value = int('1000', 2) if bmp[y][x] == 0 else 0
    delta_p = next_p[0] - prev_p[0] + (next_p[1] - prev_p[1])*1J
    bits = delta_to_bits[delta_p]
    print(delta_p, bits, value, bits+value)
    prev_p = next_p
    all_bits.append(bits+value)
if len(all_bits) % 2 != 0:
    all_bits.append(0)

all_hex_pairs = []
for i in range(0, len(all_bits), 2):
    first = all_bits[i]
    second = all_bits[i+1]
    first_mod = first << 4
    together = first_mod+second
    hex_s = hex(together)[2:]
    all_hex_pairs.append(f'{hex_s:>02}')
    print(hex(together), all_hex_pairs[-1])
data_string = ''.join(all_hex_pairs)
print(len(data_string))
print(data_string)
i = int(f'0x{data_string}',16)
print(i)
print(len(str(i)))


data_bytes = bytes.fromhex(data_string)

import binascii
b64 = binascii.b2a_base64(data_bytes, newline=False) 
print('BASE64', len(b64))
print(b64)
print()

encoded2 = binascii.b2a_base64(binascii.rlecode_hqx(data_bytes), newline=False)
print('RLE & BASE64', len(encoded2))
print(encoded2)

#assert(data_bytes.hex() == data_string)
#data_hex = data_bytes.hex()
#for i, h in enumerate(data_hex):
#    v = int(f'{h:0>2}',16) if i%2==0 else int(h,16) 
#    print(' ', h, v)
#    print('>', all_hex_pairs[i//2])
#
#bits_to_delta = {hex(v):k for k,v in delta_to_bits.items()}
#print(bits_to_delta)

    
    

    




