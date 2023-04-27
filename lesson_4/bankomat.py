s = int(input())
k=0
n=0
f=0
i=0
j=0
p=0
while s>0:
    if s//1000:
        k = s//1000
        s = s-k*1000
    elif s//500:
        n = s//500
        s = s-n*500
    elif s//200:
        d = s//200
        s = s-d*200
    elif s//100:
        f = s//100
        s = s-f*100
    elif s//50:
        i = s//50
        s = s-s*50
    elif s//20:
        j=s//20
        s=s-j*20
    elif s//10:
        p = s//10
        s=s-s*10
    else:
        print(s)
print("1000-",k)
print("500-",n)
print("200-",f)
print("100-",i)
print("50-",j)
print("10-",p)
        
    