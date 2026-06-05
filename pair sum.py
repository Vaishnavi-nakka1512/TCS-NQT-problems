a=list(map(int,input().split()))
s=int(input())
for i in range(len(a)):
    for j in range(i+1,len(a)-1):
        if a[i]+a[j]==s:
            print(a[i],a[j])
            break
            