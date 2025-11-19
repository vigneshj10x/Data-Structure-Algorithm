def rabin(t,p,base=256,mod=10**9+7):
    n,m=len(t),len(p)
    th=ph=0
    h=1
    for i in range(m-1):
        h=(h*base)%mod
    for i in range(m):
        ph=(ph*base+ord(p[i]))%mod
        th=(th*base + ord(t[i]))%mod

    for i in range(n-m+1):
        if th==ph:
            if t[i:i+m]==p:
                print("found the match at index :",i)
        if i<n-m:
            th=(th-ord(t[i])*h)%mod
            th=(th*base + ord(t[i+m]))%mod
            th=(th + mod)%mod
rabin('hellohello', 'llo')
