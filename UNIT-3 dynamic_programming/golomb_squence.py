def golomb_squence(n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=1+dp[i-dp[dp[i-1]]]
    return dp
print(golomb_squence(10))
