def solutions():
    # input
    n, k, q = input().split()
    n, k, q = int(n), int(k), int(q)
    temps= [None] * n
    for i in range(n):
        temps[i] = [int(num) for num in input().split()]
    querys = [None] * q
    for i in range(q):
        querys[i] = [int(num) for num in input().split()]
    # difference array
    diff_array = [0] * (200002)
    for lr, hr in temps:
        diff_array[lr] += 1
        diff_array[hr + 1] -= 1
    for i in range(1, len(diff_array)):
        diff_array[i] = diff_array[i - 1] + diff_array[i]
    # transfer to binary
    for i in range(1, len(diff_array)):
        if diff_array[i] >= k:
            diff_array[i] = 1
        else:
            diff_array[i] = 0
    # prefix sum
    for i in range(1, len(diff_array)):
        diff_array[i] = diff_array[i - 1] + diff_array[i]
    # query the answers
    for lr, hr in querys:
        print(diff_array[hr] - diff_array[lr - 1])
solutions()
