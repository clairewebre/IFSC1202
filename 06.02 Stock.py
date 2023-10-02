def percentchange(today, previous):
    return ((today - previous)/previous)*100

print ("{:>10s}{:>10s}".format("Price","Change"))
stockfile = "06.02 Stock.txt"
stock = open(stockfile, "r")
t = stock.readline()
t = float(t)
print("{:10.2f}".format(t))
y = t
t = stock.readline()
while t != "":
    t = float(t)
    print ("{:10.2f}{:10.2f}".format(t,percentchange(t, y)))
    y = t
    t = stock.readline()