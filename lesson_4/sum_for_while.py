a = [34,56,78,98,45,100]
s = 0

for i in a:
    s += i

print(s)
print()
n=0
b = len(a)
s=0
while n<b:
    s += a[n]
    n += 1
print(s)