def min_coins(c,a):
    dp=[10**9]*(a+1)
    dp[0]=0
    for coin in c:
        for i in range(coin,a+1):
            dp[i]=min(dp[i],dp[i-coin]+1)
    if dp[a]!=10**9:
        return dp[a]
    else:
        return "not found"

coins = [1, 2, 5]
amount = 11
print(min_coins(coins, amount))  
