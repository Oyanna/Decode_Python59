a = 1
while a < 5:
    a += 1      #2          3         4
    if a == 3:  #2==3 false 3==3 true 4==3 false
        continue
    print(a)     #2                   4   5