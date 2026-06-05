a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
for i in b:
    if i in a:
        count+=1
if count==len(b):
    print('yes')
else:
    print('no')

#----------------or------------------#

a=list(map(int,input().split()))
b=list(map(int,input().split()))
f=True
for i in b:
    if i in a:
        pass
    else:
        f=False
        break
if f==True:
    print('yes')
else:
    print('no')
