
test = open("test.txt",encoding="UTF-8", mode="r")
for line in test:
    test = list(map(int,test.read().split()))
    print(test)

b = open("output.txt", mode = "w",encoding = "UTF-8")

for i in range(3):
    fizz,bizz,n = map(int,'2,5,18'.split())
    for j in range(1,n+1):
        if j%fizz==0 and j%buzz==0:
            print("FB", end=" ")
        elif j%fizz==0:
            print("F", end = " ")
        elif j%buzz==0:
            print("B", end=" ")
        else:
            print(j, end = " ")
            
b.close()
    