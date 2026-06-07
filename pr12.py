def fun(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial =", fact)
num = int(input("Enter a number: "))
fun(num)