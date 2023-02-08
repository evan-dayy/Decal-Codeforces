n, k = input().split()
n, k = int(n), int(k)
nums = input().split()
nums = [int(num) for num in nums]

def sw(nums, n, k):
    curr = 0
    left = right = 0
    res = None
    _min = float("inf")
    while right < n:
        curr += nums[right]
        if right - left + 1 > k:
            curr -= nums[left]
            left += 1
        if right - left + 1 == k and curr < _min:
            _min = min(_min, curr)
            res = left
        right += 1
    print(res + 1)

sw(nums, n, k)

