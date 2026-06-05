n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y))
for i in range(len(a)):
    x,y=a[i]
    for j in range(i+1,len(a)):
        if a[j]==(y,x):
            print(a[i],end=',')











