def sundaram(N):
    n=(N-1)//2
    mark=[False]*(n+1)

    for i in range(1,n+1):
        j=1
        while i+j+2*i*j<=n:
            mark[i+j+2*i*j]=True
            j+=1

    prime=[2]
    for i in range(1,n+1):
        if not mark[i]:
            prime.append(2*i+1)
    return prime

p=[]
p=sundaram(20)
print(p)
            
        
