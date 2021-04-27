n = int(input())
a = input().split()
for i in range(0, a):
    if i%2 == 0:
        print(int(a[i]), end=" ")
