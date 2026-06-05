a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    max_s=a[i]
    b.append(max_s)
    for j in range(i+1,len(a)):
        max_s*=a[j]
        b.append(max_s)
print(max(b))
    

