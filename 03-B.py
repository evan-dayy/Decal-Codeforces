from heapq import *
number_test_case = int(input())
def solutions():
    n = int(input())
    monsters = [int(num) for num in input().split()]
    heap = []
    for mon in monsters:
        heappush(heap, mon)
    res = 0
    while heap:
        curr = heappop(heap)
        res += 1
        if curr == 1:
            if heap:
                nxt = heappop(heap)
                nxt -= 1
                if nxt != 0:
                    heappush(heap, nxt)
    print(res)

for _ in range(number_test_case):
    solutions()
