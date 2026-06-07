def fun(no1,no2,no3):
    if no1>no2 and no1>no3:
        print("no1 is greater")
    elif no2>no1 and no2>no3:
        print("no2 is greater")
    else:
        print("no3 is greater")
fun(no1=int(input("no1:")),no2=int(input("no2:")),no3=int(input("no3:")))