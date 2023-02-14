n, t = [int(num) for num in input().split()]

def solutions(n, t):
    nums = [int(num) for num in input().split()]
    left = right = 0
    curr = 0
    res = 0
    while right < n:
        curr += nums[right]
        while left <= right and curr > t:
            curr -= nums[left]
            left += 1
        res = max(right - left + 1, res)
        right += 1
    return res


print(solutions(n, t))

