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

inv_mod(345,3457)
