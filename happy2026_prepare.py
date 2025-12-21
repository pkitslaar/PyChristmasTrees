# small digits 2026
TARGET = \
"""
─┐┌─┐─┐┌─┐
┌┘│ │┌┘├─┐
└─└─┘└─└─┘
"""

TARGET_GRID  = {}
for y, line in enumerate(TARGET.strip().splitlines()):
    for x, char in enumerate(line):
        TARGET_GRID[(x, y)] = char

box_drawing_characters_list = [
    "─", "│", "┌", "┐", "└", "┘", "├", #"┤", "┬", "┴", "┼", 
    " ", "*"
]
box_drawing_characters = "".join(box_drawing_characters_list)
character_connections = {
    "─": {"left", "right"},
    "│": {"up", "down"},
    "┌": {"right", "down"},
    "┐": {"left", "down"},
    "└": {"up", "right"},
    "┘": {"up", "left"},
    "├": {"up", "down", "right"},
    #"┤": {"up", "down", "left"},
    #"┬": {"left", "right", "down"},
    #"┴": {"left", "right", "up"},
    #"┼": {"up", "down", "left", "right"},
    " ": {},
    "*": {},
}

# create compact connetion table by enconding the directions into 4 bits
direction_bits = {
    "up": 1,
    "down": 2,
    "left": 4,
    "right": 8,
}
character_connections_bits = {}
for char, directions in character_connections.items():
    bits = 0
    for direction in directions:
        bits |= direction_bits[direction]
    character_connections_bits[char] = f'{bits:02x}'


GRID_SIZE_X= max(x for x,y in TARGET_GRID.keys()) + 1
GRID_SIZE_Y= max(y for x,y in TARGET_GRID.keys()) + 1

import time
def plot_grid(grid):
    print("\033[?25l", end="")
    print("\033[H", end="")  # Move cursor to top-left
    # hide cursor
    print("\033[?25l", end="")
    time.sleep(0.01)
    print_chars = []
    #print_chars.append("\n" * 2)
    for y in range(GRID_SIZE_Y):
        row = []
        for x in range(GRID_SIZE_X):
            if grid.get((x, y), " ") == TARGET_GRID[(x, y)]:
                row.append("\033[92m" + grid.get((x, y), " ") + "\033[0m")
            else:
                row.append(grid.get((x, y), " "))
        print_chars.append("".join(row)+"\n")
    #print_chars.append("\n" * 2)
    print("".join(print_chars))




import random
def solve(seed, plot=False):
    random.seed(seed)
    from heapq import heappop, heappush
    front_nodes = [(0, 0, 0)]
    grid = {}#(0,0): TARGET_GRID[(0,0)]}
    while front_nodes and any(grid.get(pos) != TARGET_GRID[pos] for pos in TARGET_GRID):
        t, x, y = heappop(front_nodes)
        if (x, y) in grid and grid[(x, y)] == TARGET_GRID[(x, y)]:
            continue
        char_candidate_votes = {bc: 1 for bc in box_drawing_characters}
        for neighbor_info in [(x-1,y, "right"),(x+1,y,"left"),(x,y-1,"down"),(x,y+1,"up")]:
            neighbor, direction = (neighbor_info[0], neighbor_info[1]), neighbor_info[2]
            if neighbor in grid:
                n_char = grid[neighbor]
                for bc in box_drawing_characters:
                    vote_weight = 1
                    if direction in character_connections[bc]:
                        vote_weight += 2
                    char_candidate_votes[bc] = char_candidate_votes.get(bc, 0) + vote_weight

        
        # Normalize votes to probabilities
        total_votes = sum(char_candidate_votes.values())
        char_probabilities = {k: v / total_votes for k, v in char_candidate_votes.items()}
        chars, probs = zip(*char_probabilities.items())
        char = random.choices(chars, probs)[0]
        grid[(x, y)] = char
        if plot:
            plot_grid(grid)
        # Add neighboring nodes to the front
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE_X and 0 <= ny < GRID_SIZE_Y:
                heappush(front_nodes, (t + 1 + random.randint(0,5), nx, ny))
    if plot:
        plot_grid(grid)
    return grid

def solve_simple(seed, plot=False):
    random.seed(seed)
    T = TARGET_GRID
    G = {}.fromkeys(TARGET_GRID, ' ')
    N=[(0,0)]
    while G!=T and N:
        p=N.pop(0)
        if G[p]!=T[p]:
            G[p] = random.choice(box_drawing_characters)
        N.extend(q for q in T if G[q]!=T[q] and abs(q[0]-p[0])+abs(q[1]-p[1])==1)
        #for dx,dy in[(-1,0),(1,0),(0,-1),(0,1)]:
        #    q=p[0]+dx,p[1]+dy
        #    if (q)in G and G[q]!=TARGET_GRID[q]:
        #        N.append(q)
        if plot:
            plot_grid(G)
    if plot:
        plot_grid(G)
    return G

if __name__ == "__main__":
    #print("\033[?25h", end="")

    draw = False
    seed = 123
    while False:
        result_grid = solve_simple(seed, plot=False)
        if all(result_grid.get(pos) == TARGET_GRID[pos] for pos in TARGET_GRID):
            if draw:
                # clear screen
                print("\033[2J", end="")  # Clear screen
                solve_simple(seed, plot=False)
                # show cursor
            print("\033[?25h", end="")
            print(f"Solved with seed {seed}!")
            #plot_grid(result_grid)
            break
        seed += 1

    # final solution
    PY = []
    S_str = str(seed)
    #PY.append(f"import random as R;R.seed({S_str});")
    X_str = str(GRID_SIZE_X)
    Y_str = str(GRID_SIZE_Y)
    B_str = f"{''.join(character_connections_bits.keys())}"
    C_str = f"{''.join(character_connections_bits.values())}"

    CLEAR_SCREEN_CODE = '\033[2J'
    CURSOR_HOME_CODE = '\033[H'
    HIDE_CURSOR_CODE = '\033[?25l'
    SHOW_CURSOR_CODE = '\033[?25h'
    COLOR_RESET_CODE = '\033[0m'
    COLOR_GREEN_CODE = '\033[92m'
    COLOR_RED_CODE = '\033[91m'
    COLOR_GOLD_CODE = '\033[93m'

    #T_help_str = "".join(TARGET_GRID[(x, y)] for y in range(GRID_SIZE_Y) for x in range(GRID_SIZE_X))
    #T_help_str = '─┐┌─┐─┐┌─┐┌┘│ │┌┘├─┐└─└─┘└─└─┘'
    T_help_str = '─┐┌─┐─┐┌─┐\\n┌┘│ │┌┘├─┐\\n└─└─┘└─└─┘'
    
    #T_str = f"{{(i%{X_str},i//{X_str}):c for i,c in e(\"{T_help_str}\")}}"
    T_str = f"[*'{T_help_str}']"
    #PY.append()
    #G_str = "{k:' 'for k in T}"
    G_str = f"[' ']*32"
    #PY.append(f"G={G_str}")

    B_str = "├─│┌┐└┘"##$%&()@!^"  # extra chars to avoid mod bias

    PY.append(f"R,T,G,P,r=0,{T_str},{G_str},print,range")
    PY.append(f"G[10]=G[21]='\\n';P('{CLEAR_SCREEN_CODE}{HIDE_CURSOR_CODE}')")

    #PY.append(f"N,R,T=[0],1,{T_str}")
    #PY.append(f"G=[' \\n'[c=='\\n'] for c in T]")


    #print_helper_str = ""
    #print_helper_str = "import time;time.sleep(0.01);print('\033[H',end='');"
    #print_helper_str = "P('\033[H',end='');"
    #print_grid_str = f"def O(g):{print_helper_str}[print(c,end=''if (i+1)%{X_str} else'\\n')for i,c in enumerate(g)]"    
    #print_grid_str = f"def O(g):{print_helper_str}print(''.join(g))"    
    #PY.append(f"{print_grid_str}")
    #PY.append("O(T);print(len(T))")



    #PY.append(f"")  # hide cursor

    #PY.append("O(G);print(len(G))")

    #PY.append(f"N=[(0,0)]")
    PY.append(f"while G!=T:")
    #PY.append(f" p=N.pop(0);R+=1")
    PY.append(f" p=R%{len(eval(T_str))};R+=15")
    PY.append(f" if G[p]!=T[p]:")
    PY.append(f"  G[p]='{B_str}'[R%{len(B_str)}]")
    #PY.append(" N.extend(q for q in T if G[q]!=T[q] and abs(q[0]-p[0])+abs(q[1]-p[1])==1) ")
    #PY.append(f" N+=[q for q in r({len(eval(T_str))})if G[q]!=T[q]]")# and abs(q-p)==1) ")
    #PY.append(" for dx,dy in[(-1,0),(1,0),(0,-1),(0,1)]:")
    #PY.append("  q=p[0]+dx,p[1]+dy")
    #PY.append("  if (q)in G and G[q]!=T[q]:")
    #PY.append("   N.append(q)")
    
    #PY.append("   N+=[q]") 
    delay_Str = ""
    delay_Str = ";sum(r(20<<17))"
    #delay_Str = ";import time as t;t.sleep(0.05)"
    #PY.append(f" P('{CURSOR_HOME_CODE}'+''.join(G)){delay_Str}")  # delay
    PY.append(f" P('{CURSOR_HOME_CODE}',*[[c,f'\033[9{{p%5}}m{{c}}{COLOR_RESET_CODE}',c][c==t] for c,t in zip(G,T)],sep=''){delay_Str}")  # delay
    #PY.append(" O(G)")
    PY.append(f"P('{SHOW_CURSOR_CODE}')")  # show cursor
    #PY.append(" O(T)")



    
    PY_SOURCE = "\n".join(PY)
    print(PY_SOURCE.replace('\033', '\\033'))

  

    exec(PY_SOURCE)


    with open("happy2026.py", "wb") as f:
        f.write(PY_SOURCE.encode("utf-8"))

    print("\n--- Generated Source Code ---\n")

    print(len(PY_SOURCE))

    print(PY_SOURCE.replace('\033', '\\033'))
