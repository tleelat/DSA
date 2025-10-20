## Count Digits in a number using Recursion 

## Constraints : 
    # 1 <= 'T' <= 1000
    # 1 <= ‘X’ <= 10^18
    # Time Limit: 1 sec

def countDigits(n):
    cnt = 0
    while n > 0:
        cnt = cnt + 1
        n = n // 10
    return cnt
pass