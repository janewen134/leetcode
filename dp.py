import numpy as np
# O(n) space complexity
def climb_stairs(n):
    # edge case
    if (n <= 2):
        return n
    # init
    dp = [1] * (n+1)
    # state update
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    # answer
    # print(dp)
    return dp[n]
# O(1) space complexity
def climb_stairs2(n):
    # edge case    
    if (n<=2):
        return n
    # one step before, and two steps before
    last_1, last_2 = 2, 1
    current = 0
    for i in range(2, n):
        current = last_1 + last_2
        last_2 = last_1
        last_1 = current
        # print('i: ',i)
        # print(last_2)
        # print(last_1)
        # print(current)
    return current
   
def rob_house(n):
    if len(n) == 0:
        return 0
    
    last_1,last_2 = 0,0
    curr = 0

    for i in n:
        curr = max(last_1, i+last_2)
        last_2=last_1
        last_1=curr
    print(curr)
    return curr


# def numDecodings(s: str) -> int:
#     n = len(s)
#     # a = f[i-2], b = f[i-1], c = f[i]
#     a, b, c = 0, 1, 0
#     for i in range(1, n + 1):
        # c = 0
    #     if s[i - 1] != '0':
    #         c += b
    #     if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
    #         c += a
    #     a, b = b, c
    # return c

def numDecodings(s: str) -> int:
    n = len(s)
    f = [1] + [0] * n
    for i in range(1, n + 1):
        if s[i - 1] != '0':
            f[i] += f[i - 1]
        if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
            f[i] += f[i - 2]
    return f[n]

def mySqrt(a: int) -> int:
    if(a == 0 or a == 1):
        return a
    l,r, mid, sqrt = 1, a, 0, 0
    while(l <= r):
        mid = l + (r - l)//2
        sqrt = a // mid
        # print(sqrt)
        if (sqrt == mid):
            return mid
        elif (mid > sqrt):
            r = mid - 1
        else:
            l = mid + 1
        
    return r


if __name__ == "__main__":
    # a = climb_stairs2(5)
    # a = rob_house([1])
    # a = numDecodings("226")
    a = mySqrt(16)
    print(a)
