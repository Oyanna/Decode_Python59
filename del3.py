n = int(input())
s = input()
s = s.split()
nums = []
mx = int(s[0])
mn = int(s[0])
for i in s:
    nums.append(int(i))
for i in nums:
    if i > mx:
        mx = i
    if i < mn:
        mn = i
print((mx - mn + 1) - n)