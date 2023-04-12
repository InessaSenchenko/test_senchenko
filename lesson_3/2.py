# не парне, кратне 3, кратне 5, не кратне 10
x = int(input(" Enter a number "))

if (x%2 and not x%3 and not x%5 and x%10):
    print(x)