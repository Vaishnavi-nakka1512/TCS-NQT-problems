a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        print(i,a.count(i))
        b.append(i)
        