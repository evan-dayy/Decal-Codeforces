s = input()
n = int(input())
res = [0] * len(s)
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        res[i] = 1 + res[i - 1]
    else:
        res[i] = res[i - 1]
 
for _ in range(n):
    left, right = input().split()
    left, right = int(left), int(right)
    print(res[right - 1] - res[left - 1])
