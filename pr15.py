def fun(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s
num = int(input("Enter a number: "))
print("Sum =", fun(num))