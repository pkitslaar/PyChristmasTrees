# small digits 2026
TARGET = \
"""
─┐┌─┐─┐┌─┐
┌┘│ │┌┘├─┐
└─└─┘└─└─┘
"""


if __name__ == "__main__":

    # final solution

    CLEAR_SCREEN_CODE = '{E}2J'
    CURSOR_HOME_CODE = '{E}H'
    HIDE_CURSOR_CODE = '{E}?25l'
    SHOW_CURSOR_CODE = '{E}?25h'
    COLOR_RESET_CODE = '{E}0m'
    T_help_str = '─┐┌─┐─┐┌─┐\\n┌┘│ │┌┘├─┐\\n└─└─┘└─└─┘'
    T_str = f"[*'{T_help_str}']"
    G_str = f"[' ']*32"
    B_str = "├─│┌┐└┘"##$%&()@!^"  # extra chars to avoid mod bias

    PY = []
    PY.append(f"E,R,T,G,P,r='\033[',1,{T_str},{G_str},print,range")
    PY.append(f"G[10::11]='\\n'*2;P(f'{CLEAR_SCREEN_CODE}{HIDE_CURSOR_CODE}')")
    PY.append(f"while G!=T:")
    PY.append(f" p=R%{len(eval(T_str))};R+=15")
    PY.append(f" if G[p]!=T[p]:")
    PY.append(f"  G[p]='{B_str}'[R%{len(B_str)}]")
    delay_Str = "]*(30<<19)"
    PY.append(f" [P(f'{CURSOR_HOME_CODE}',*[[c,f'{{E}}9{{p%5}}m{{c}}{COLOR_RESET_CODE}'][c==t]for c,t in zip(G,T)],sep=''){delay_Str}")  # delay
    PY.append(f"P(f'{SHOW_CURSOR_CODE}')")  # show cursor
    
    PY_SOURCE = "\n".join(PY).replace('\033', '\\033')
    exec(PY_SOURCE)

    with open("happy2026.py", "wb") as f:
        f.write(PY_SOURCE.replace('\033', '\\033').encode("utf-8"))

    print("\n--- Generated Source Code ---\n")

    print(len(PY_SOURCE))

    print(PY_SOURCE)
