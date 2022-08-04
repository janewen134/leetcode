import numpy as np
def climb(n):
    if (n <= 2):
        return n
    dp = [1] * (n+1)
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]

if __name__ == "__main__":
    a = climb(5)
    print(a)