number_test_case = int(input())

def solutions():
    return
for _ in range(number_test_case):
    n, m, k = [int(num) for num in input().split()]
    mat = [["."] * m for _ in range(n)]
    for i in range(n):
        mat[i] = list(input())
    print(mat)
    print(solutions())

