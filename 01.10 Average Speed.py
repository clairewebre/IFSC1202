l = input("Enter length of race in kilometers: ")
m = float(input("Enter minutes: "))
s = float(input("Enter seconds: "))
miles = float(l) / 1.61
hours = float(m / 60 ) + float(s / 3600)
mph = float(miles) / float(hours)
print(float(mph))