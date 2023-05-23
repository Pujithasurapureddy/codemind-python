n=int(input())
s=0
m=1
while n!=0:
    rem=n%10
    s=s+rem
    m=m*rem
    n=n//10
if(s==m):
    print("Spy Number")
else:
    print("Not Spy Number")