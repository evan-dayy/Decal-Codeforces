from itertools import groupby
from heapq import *
number_test_case = int(input())
def solutions():
    n = int(input())
    s = input()
    n_sheep = sum(1 for c in s if c == "*")
    # special case
    if n_sheep == n or n_sheep == 0:
        return 0
    # general cases
    # group the count
    group = [(g, len(list(b))) for g, b in groupby(s)]
    # trying to find how many sheeps before a space or after a space
    prefix = [0] * (len(group))
    curr = 0
    heap = []
    for i, (g, length) in enumerate(group):
        if g == "*":
            curr += length
        else:
            prefix[i] = curr
            # put the gap into the heap
            heappush(heap, (length, i))

    res = 0
    while heap:
        l, i = heappop(heap)
        left_cnt, right_cnt = prefix[i], n_sheep - prefix[i]
        res += min(left_cnt, right_cnt) * l
    return res


for _ in range(number_test_case):
    print(solutions())


