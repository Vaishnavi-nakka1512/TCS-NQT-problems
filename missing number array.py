a=list(map(int,input().split()))
n=len(a)+1
A=n*(n+1)//2
P=sum(a)
M=A-P
print(M)

#-----------or-----------#

a=list(map(int,input().split()))
print(a)
b=len(a)
for i in range(1,b+1):
    if i not in a:
        print(i)
