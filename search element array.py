a=list(map(int,input().split()))
k=int(input())
for i in a:
    if k==i:
        print('found')
        break
else:
    print('not found')
