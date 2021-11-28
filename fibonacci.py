def fabonacci_seq(n):
    a=0 # first number
    b=1 # second number
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    print(a,b, end=" ")
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    print(b,end=" ")
fabonacci_seq(10)                
