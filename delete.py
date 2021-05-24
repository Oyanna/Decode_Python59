n = int(input())
a = input().split()
a.append('1')
cnt = 0
k = 0
l = []
for i in range(0, n+1):
    if a[i] == '1':
        cnt +=1
    if a[i] == '1' and cnt > 1:
        k = int(a[i-1])
        l.append(k)


print(cnt-1)
for i in range (0, len(l)):
    print(l[i], end=' ')



