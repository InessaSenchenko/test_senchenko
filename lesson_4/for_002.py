a = [10, 20, 30 ,40]
for id, item in enumerate(a):
    
    a[id] = item + 5
    if item==40:
        print(id)
print(a)
