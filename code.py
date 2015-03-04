T = int(raw_input())
for i in range (0,T):
    n,c,m = [int(x) for x in raw_input().split(' ')]
    
    ch = n/c
    w=ch
    while(w>=m):
        ch=ch+w/m
        w=w-((w/m)*m)+(w/m)
    # write code to compute answer
    print ch