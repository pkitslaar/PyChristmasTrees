# small digits 2026
TARGET = \
"""
─┐┌─┐─┐┌─┐
┌┘│ │┌┘├─┐
└─└─┘└─└─┘
"""


if __name__ == "__main__":

    # final solution

    CLEAR_SCREEN_CODE = '\033[2J'
    CURSOR_HOME_CODE = '\033[H'
    HIDE_CURSOR_CODE = '\033[?25l'
    SHOW_CURSOR_CODE = '\033[?25h'
    COLOR_RESET_CODE = '\033[0m'


    T_help_str = '─┐┌─┐─┐┌─┐\\n┌┘│ │┌┘├─┐\\n└─└─┘└─└─┘'
    T_str = f"[*'{T_help_str}']"
    G_str = f"[' ']*32"
    B_str = "├─│┌┐└┘"##$%&()@!^"  # extra chars to avoid mod bias

    PY = []
    PY.append(f"R,T,G,P,r=1,{T_str},{G_str},print,range")
    PY.append(f"G[10]=G[21]='\\n';P('{CLEAR_SCREEN_CODE}{HIDE_CURSOR_CODE}')")
    PY.append(f"while G!=T:")
    PY.append(f" p=R%{len(eval(T_str))};R+=15")
    PY.append(f" if G[p]!=T[p]:")
    PY.append(f"  G[p]='{B_str}'[R%{len(B_str)}]")
    delay_Str = ";sum(r(20<<17))"
    PY.append(f" P('{CURSOR_HOME_CODE}',*[[c,f'\033[9{{p%5}}m{{c}}{COLOR_RESET_CODE}',c][c==t] for c,t in zip(G,T)],sep=''){delay_Str}")  # delay
    PY.append(f"P('{SHOW_CURSOR_CODE}')")  # show cursor
    
    PY_SOURCE = "\n".join(PY)
    exec(PY_SOURCE)

    with open("happy2026.py", "wb") as f:
        f.write(PY_SOURCE.encode("utf-8"))

    print("\n--- Generated Source Code ---\n")

    print(len(PY_SOURCE))

    print(PY_SOURCE.replace('\033', '\\033'))
