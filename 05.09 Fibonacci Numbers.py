n = input("Enter Fibonacci Sequence Number: ")
a=0
b=1
if n == 0:
    print("Fibonacci Number: 0")
elif n == 1:
    print("Fibonacci Number: 1")
else:
    for i in range (2,int(n)+1):
        value = b + a
        a = b
        b = value
    print("Fibonacci Number: {}".format(value))