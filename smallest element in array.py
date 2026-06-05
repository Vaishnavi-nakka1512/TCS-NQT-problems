import array as ar
n=int(input('eneter'))
a=ar.array('i',[1,2,3,4,5])
print(a)
s=a[0]
for i in a:
    if i<s:
        s=i
print(s)

