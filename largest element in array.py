import array as ar
a=list(map(int,input().split()))
print(a)
s=a[0]
for i in a:
    if i>s:
        s=i
print(s)

