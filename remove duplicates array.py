a=list(map(int,input().split()))
print(a)
a=list(set(a))
print(a)

#-------------or------------#

a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
        