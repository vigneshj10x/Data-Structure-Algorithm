def lpss(p):
    m=len(p)
    lps=[0]*m
    j=0
    i=1
    while i<m:
        if p[i]==p[j]:
            j+=1
            lps[i]=j
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                lps[i]=0
                i+=1
    return lps

def kmp(t,p):
    n=len(t)
    m=len(p)
    lps=lpss(p)
    i=j=0
    while i<n:
        if p[j]==t[i]:
            j+=1
            i+=1
        if j==m:
            print("patten found at index :",i-j)
            j=lps[j-1]
        elif i<n and p[j]!=t[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
kmp('abxabcabcaby', 'abcaby')
    
