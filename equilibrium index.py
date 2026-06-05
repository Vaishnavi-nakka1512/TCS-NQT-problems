a=list(map(int,input().split()))
for i in range(len(a)):
    left=sum(a[i:])
    right=sum(a[:i+1])
    if left==right:
        print(i)
        break

#-------------or--------------#

a=list(map(int,input().split()))
for i in a:
    left=sum(a[i:])
    right=sum(a[:i+1])
    if left==right:
        print(i)
        break
    
