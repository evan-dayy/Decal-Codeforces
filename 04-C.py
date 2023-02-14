n = int(input())
from collections import defaultdict, Counter

def solutions(n):
    s = input()
    left = right = 0
    target = len(Counter(s))
    visited = defaultdict(int)
    res = float("inf")
    while right < n:
        visited[s[right]] += 1
        while left <= right and len(visited) == target:
            res = min(res, right - left + 1)
            visited[s[left]] -= 1
            if visited[s[left]] == 0:
                del visited[s[left]]
            left += 1
        right += 1
    return res
    
print(solutions(n))
