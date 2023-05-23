n=int(input())
sq=n*n
s=0
while(sq!=0):
    rem=sq%10
    s=s+rem
    sq=sq//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")