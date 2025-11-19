def sprase(m):
    n=len(m)
    col=len(m[0])
    count=0
    
    for i in range(n):
        for j in range(col):
            if m[i][j]!=0:
                count+=1
                
    k = [[0] * 3 for _ in range(count + 1)]

    s=1
    k[0][0]=n
    k[0][1]=col
    k[0][2]=count
    
    for i in range(n):
        for j in range(col):
            if m[i][j]!=0:
                k[s][0]=i
                k[s][1]=j
                k[s][2]=m[i][j]
                s+=1
    return k
            


matrix=[[0,0,3],[0,0,0],[4,0,3]]
result=[]
result=sprase(matrix)
for i in result:
    print(i)
