def inv_mod(a,b):
    B = b
    q_arr = []
    g = 1
    count = 0
    while g:
        x = b // a
        q_arr.append(x)
        g = b - (x * a)
        print(f'{b} = {x}*{a} + {g}')
        b = a
        a = g
        count += 1
    p0 = 0
    p1 = 1
    print('-------------------------------')
    print(f'p0 = {p0}')
    print(f'p1 = {p1}')
    for i in range(count-1):
        p2 = (p0 - p1*q_arr[i]) % B
        print(f'p{i+2} = {p0} - {p1}*{q_arr[i]} (mod {B}) = {p2}')
        p1, p0 = p2, p1
        
    return 0

# inv_mod(345,3457)


# x = a1 mod m1 
# x = a2 mod m2
# ...
# x = a_n mod m_n

# M = m1*...m_n 
# M_i = M / m_i 
# N_i = M_i^-1 mod m_i

# x = SUM (a_i*M_i*N_i) mod M

from functools import reduce
from itertools import count
from operator import le


def CRT(pairs):
    m_list, a_list = [p[0] for p in pairs], [p[1] for p in pairs]
    M = reduce(lambda x, y: x * y, m_list)
    print('M = ',end=' ')
    for i in range(len(m_list)):
        print(f'{m_list[i]}', end=" * ")
    print(f' = {M}')
    Mi_list = [M // x for x in m_list]
    for i in range(len(Mi_list)):
        print(f'M{i+1} = {Mi_list[i]}')
    print('----------------------------')

    Ni_list = [pow(Mi_list[i], -1 ,m_list[i]) for i in range(len(Mi_list))]
    j = 1
    for Mi, mi in list(zip(Mi_list,m_list)):
        print('____________________________________________')
        print(f'Шукаємо m{j}^1 mod M{j}:   {mi}^-1 mod {Mi}:')
        j += 1
        inv_mod(Mi,mi)
        
    X = 0
    print('X = ', end=" ")
    for i in range(len(m_list)):
        X += (a_list[i] * Mi_list[i] * Ni_list[i])
        print(f'{a_list[i]} * {Mi_list[i]} * {Ni_list[i]}', end=" + ")
    print(f'mod {M}')
    return print(f'X = {X % M}')

# usage: CRF([(m1, a1), (m2, a2), ...])
CRT([(3, 2), (5, 3), (7, 2)])
