number_test_case = int(input())

def mark(mat, r, c, m, n, k):
    # marking process
    left = 0
    rl, cl = r-1, c-1
    while 0 <= rl < m and 0 <= cl < n and (mat[rl][cl] == "*" or mat[rl][cl] == "#"):
        rl -= 1
        cl -= 1
        left += 1
    rr, cr = r-1, c+1
    right = 0
    while 0 <= rr < m and 0 <= cr < n and (mat[rr][cr] == "*" or mat[rr][cr] == "#"):
        rr -= 1
        cr += 1
        right += 1

    max_height = min(left, right)
    if max_height >= k:
        mat[r][c] = "#"
        cnt = 0
        rl, cl = r, c
        while cnt < max_height:
            mat[rl - 1][cl - 1] = "#"
            rl -= 1
            cl -= 1
            cnt += 1
        cnt = 0
        rr, cr = r, c
        while cnt < max_height:
            mat[rr - 1][cr + 1] = "#"
            rr -= 1
            cr += 1
            cnt += 1

def solutions(mat, k):
    # searching from the bottom and mark he V shape
    m, n = len(mat), len(mat[0])
    for i in range(m - 1, k-1, -1):
        for j in range(n):
            if mat[i][j] == "*" or mat[i][j] == "#":
                mark(mat, i, j, m, n, k)
    for i in range(m):
        for j in range(n):
            if mat[i][j] == "*":
                return "NO"
    return "YES"



for _ in range(number_test_case):
    n, m, k = [int(num) for num in input().split()]
    mat = [["."] * m for _ in range(n)]
    for i in range(n):
        mat[i] = list(input())
    print(solutions(mat, k))

