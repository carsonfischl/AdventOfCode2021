with open("C:\\Users\\carso\\OneDrive\\Desktop\\AdventOfCode\\2021\\day1.txt") as f:
    count = 0
    l = f.readlines()
    ll = []
    for j in l:
        num = int(j)
        ll.append(num)
    print(ll)
    for i in range(0,len(ll)):
        if sum(ll[i:i+3]) < sum(ll[i+1:i+4]):
            count += 1
    print(count)