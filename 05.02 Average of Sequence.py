n=input("Enter Number (CR to quit): ")
sum=0
count=0
while n != '':
    sum += int(n)
    count+=1
    n=input("Enter Number (CR to quit): ")
if count != 0:
    average = sum/count
    print("Average: {}".format(average))
else:
    print("Sequence length is 0")