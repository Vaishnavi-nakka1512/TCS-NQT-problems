n=int(input('enter'))
a=list(map(int,input().split()))
a.sort()
med=0
if n%2==0:
    i=n//2-1
    med=a[i]
else:
    j=n//2
    med=a[j]
print(med)
