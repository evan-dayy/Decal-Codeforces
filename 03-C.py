from heapq import *
number_test_cases = int(input())
 
def solutions():
    flag = False
    x, n, m = [int(num) for num in input().split()]
    while n > 0 and x > 20:
        x = x // 2 + 10
        n -= 1
    while m > 0:
        x -= 10
        if x <= 0:
            print("YES")
            flag = True
            break
        m -= 1
    if not flag:
        print("NO")
 
 
for _ in range(number_test_cases):
    solutions()
