a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            break
    else:
        print(a[i],end=',')
        
#--------------or--------------#

a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]==max(a[i:]):
        print(a[i],end=',')


                
