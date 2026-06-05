a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=list(set(a))
b1=list(set(b))
print(*list(set(a1+b1)))
for i in a1:
    if i in b1:
        print(i,end=',')