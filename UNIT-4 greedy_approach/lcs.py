def lcs(x,y):
    m=len(x)
    n=len(y)
    dp=[]
    for i in range(m+1):
        row=[]
        for j in range(n+1):
            row.append(0)
        dp.append(row)

    for i in range(1,m+1):
        for j in  range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    i=m
    j=n
    res=[]
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            res.append(x[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    res.reverse()
    return dp[m][n],"".join(res)


X = "ABCBDAB"
Y = "BDCABA"
length,result= lcs(X, Y)
print("LCS Length  :", length)
print("LCS sequence:",result)

            
