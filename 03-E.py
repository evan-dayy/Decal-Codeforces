import math
number_test_case = int(input())

def solutions(nums, n, x):
    ans = 0
    i = curr = cnt = 0
    while i < n:
        if i > 0 and nums[i] != nums[i - 1]:
            curr = cnt * nums[i]
        curr += nums[i]
        cnt += 1
        if curr >= x:
            ans += 1
            i += 1
            curr = 0
            cnt = 0
            continue
        i += 1
    return ans

for _ in range(number_test_case):
    n, x = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    nums.sort(reverse = 1)
    print(solutions(nums, n, x))

