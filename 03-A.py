deno = [100, 20, 10, 5, 1]
def solutions():
    num = int(input())
    res = 0
    while num:
        for d in deno:
            if d <= num:
                res += num // d
                num %= d
    return res
print(solutions())
    

