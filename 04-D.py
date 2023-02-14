n = int(input())
s = input()
cases = int(input())


def solutions(s, k, char):
    left = right = 0
    res = 0
    cnt = 0
    while right < len(s):
        if s[right] == char:
            cnt += 1
        while right - left + 1 - cnt > k:
            if s[left] ==  char:
                cnt -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res

for _ in range(cases):
    k, char = input().split()
    k = int(k)
    print(solutions(s, k, char))

