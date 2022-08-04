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
if __name__ == "__main__":
    # a = climb_stairs2(5)
    a = rob_house([1])
    print(a)