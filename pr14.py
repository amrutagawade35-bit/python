def fun(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    print("Sum of digits =", s)
num = int(input("Enter a number: "))
fun(num)