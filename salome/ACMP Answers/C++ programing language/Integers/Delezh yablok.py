n,k=map(int,input().split())
a=k//n
b=k%n
if k%n:
    c=k%n
else:
    c=0
 
if c==0:
    l=0
else:
    l=n-c
print(a,c,l)
