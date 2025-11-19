def navie(t,p):
    n=len(t)
    m=len(p)
    for i in range(n-m+1):
        res=True
        for j in range(m):
            if p[j]!=t[i+j]:
                res=False
                break
        if res:
            print("match found at index :",i)

navie("abababab",'aba')
