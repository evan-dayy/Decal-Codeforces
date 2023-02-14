n, m = [int(num) for num in input().split()]

def isValid(r, nums, rad):
    curr = 0
    completed = 0
    while curr < len(rad) and completed < len(nums):
        lwr = rad[curr] - r
        hig = rad[curr] + r
        while completed < len(nums) and lwr <= nums[completed] <= hig:
            completed += 1
        if completed == len(nums):
            break
        curr += 1
    return completed == len(nums)

def solutions(m, n):
    nums = [int(num) for num in input().split()]
    rad = [int(num) for num in input().split()]
    left = 0
    right = 2 * 10 ** 9 + 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if isValid(mid, nums, rad):
            right = mid
        else:
            left = mid
    if isValid(left, nums, rad):
        return left
    return right

print(solutions(m, n))
