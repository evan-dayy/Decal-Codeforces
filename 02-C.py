n, k = input().split()
n, k = int(n), int(k)
lectures = [int(num) for num in input().split()]
awake = [int(num) for num in input().split()]

def max_lectures(n, k, lectures, awake):
    res = float("-inf")
    total_prefix = [0] * len(lectures)
    partial_prefix = [0] * len(lectures)
    total_prefix[0] = lectures[0]
    partial_prefix[0] = lectures[0] if awake[0] else 0
    
    for i in range(1, len(lectures)):
        total_prefix[i] = total_prefix[i - 1] + lectures[i]
        partial_prefix[i] = partial_prefix[i - 1] if awake[i] == 0 else partial_prefix[i - 1] + lectures[i]

    
    for j in range(k - 1, len(lectures)):
        res = max(res,
                  total_prefix[j] -
                  (total_prefix[j - k] if j - k >= 0 else 0) +
                  (partial_prefix[j - k] if j - k >= 0 else 0) +
                  partial_prefix[-1] - partial_prefix[j])
        
                  
    print(res)

    
max_lectures(n, k, lectures, awake)
