with open("C:\\Users\\carso\\OneDrive\\Desktop\\AdventOfCode\\2021\\day2.txt") as f:
    h = 0 #horizontal position
    d = 0 #depth position
    a = 0 #aim value
    l = f.readlines()
    for j in l:
        if 'forward' in j:
            h += int(j.split()[1])
            d += a*int(j.split()[1])
        if 'up' in j:
            #d -= int(j.split()[1]) for first part
            a -= int(j.split()[1])
        if 'down' in j:
            #d += int(j.split()[1]) for first part
            a += int(j.split()[1])
        
    print('a:', a)
    print('d:', d)
    print('h:', h)
    print(d*h)