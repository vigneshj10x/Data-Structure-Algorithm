def ugly(n):
    ugly_number=[0]*n
    ugly_number[0]=1
    i2=i3=i5=0
    n2,n3,n5=2,3,5
    for i in range(1,n):
        ugly_n=min(n2,n3,n5)
        ugly_number[i]=ugly_n
        if ugly_n==n2:
            i2+=1
            n2=ugly_number[i2]*2
        if ugly_n==n3:
            i3+=1
            n3=ugly_number[i3]*3
        if ugly_n==n5:
            i5+=1
            n5=ugly_number[i5]*5
    return ugly_number[-1]
print(ugly(55))