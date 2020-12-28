g,x,y=[['0']*12 for _ in[0]*12],[0],[2]
def P(d):[x,y][d in'^v'][0]+=(d not in'0')*(-1)**(d in'^<')
def r(c,d):g[y[0]][x[0]]=c;P(d)
I=dict(zip('0><v^','0<>^v'))
two='1^***>,8v*|*>,2v*/>,1v***0,3<*--*v,1>*\\\\*v,1v**<,2^*|<,6^*|*<,1^*\\*<,1<**v,1>*\\\\v,3<*-*v,1v**>,2^*\\>,8^*|*>,1^***0'
#two_bin='0b  00     00          0       000'
#             ^^     ^^          ^       ^^^
#           times   direction   turn   pattern (3)
#        1  00     ^ 00        L 0     (skip) 000
#        2  01     v 01        R 1     *--*   001 and direction in ><
#        4  10     > 10                *|*    001 and direction in v^
#        8  11     < 11                *//*   010 and direction in <> and turn left
#                                      *//*   010 and direction in ^v and turn right
#                                      *\\*   010 and direction in <> and turn right           
#                                      *\\*   010 and direction in ^v
#                                      */     101
#                                      *\\*   110
#                                      *//*   111
two_bin=[
0b00001000, # 1^***>
0b11010001, # 8v*|*>
0b01010011, # 2v*/v
0b00011000, # 1v***0
0b01110001, # 2<*--*v
0b00110001, # 1<*--*v
0b00101010, # 1>*\\\\*v
0b00001100, # 1v**<
0b11000001, # 8^*|*<
]
def parse_time(intcode):
    times = 2**((intcode&192)>>6)
    return times

def parse_direction(intcode):
    direction = (intcode&48)>>4
    return direction

def parse_turn(intcode):
    return (intcode&8)>>3

def parse_pattern(intcode):
    return (intcode&7)

def test_parse():
    assert(1 == parse_time     (0b00000000))
    assert(2 == parse_time     (0b01000000))
    assert(4 == parse_time     (0b00000000))
    assert(0 == parse_direction(0b00000000))
    assert(1 == parse_direction(0b00010000))
    assert(2 == parse_direction(0b00100000))
    assert(3 == parse_direction(0b00110000))
    assert(0 == parse_turn     (0b00000000))
    assert(1 == parse_turn     (0b00001000))
#for times,d,*w,e in two.split(','):
for int_code in two_bin:
    times = parse_time(int_code)
    d = '^v><'[parse_direction(int_code)] 
    turn = 'LR'[parse_turn(int_code)]
    e = {
        ('^','L'): '<',
        ('v','L'): '>',
        ('v','R'): '<',
        ('^','R'): '>',
        ('>','L'): '^',
        ('>','R'): 'v',
        ('<','L'): 'v',
        ('<','R'): '^'
    }[(d,turn)]
    pattern=parse_pattern(int_code)
    if pattern > 0:
        if d in '><':
            w = {1: '*--*',2:'*//*', 3: '*/'}[pattern]
        else:
            w = {1: '*|*',2:'*\\\\*', 3: '*\\'}[pattern]
    else:
        w = '***'
    #d,*c,e = content
    for _ in[0]*int(times):
        [r(c,d) for c in w]
        P(e)
        d=I[d]
        P(d)
        w=w[::-1]
        
        print('\n'.join([''.join(r) for r in g]))
        print()
two=r"""
 0123456789
0**********
1*||||||//*
2*******--*
3      *--*
4      *--*
5*******\\*
6*\\||||||*
7*--*******
8*--*
9*--*******
0*//||||||*
1**********
"""
two_pseudo_code = """
SET_POS_YX 0,0 # could be assume
1*(DRAW_Y+ '***'; INC X) or 3*('*';Y+;X0) + 1*(' ';Y0;X+)
6*(DRAW_Y+ '*|*'; INC X) or 6*()
2*(DRAW_Y+ '*/ ' ; INC X)
1*(DRAW_Y+ '** ' ; INC X)
SET_POS_YX 2,6 or 
3*(DRAW_X+, '*--*'; INC Y)
SET_POS_YX 5,9
1*(DRAW_Y+ '***'; DEC X)
2*(DRAW_Y+ '\|*'; DEC X)
4*(DRAW_Y+ '*|*'; DEC X)

"""
zero=r"""
**********
*//||||\\*
*--****||*
*--*  *--*
*--*  *--*
*--*  *--*
*--*  *--*
*\\|||*//*
**********
"""
print(two)
print(zero)