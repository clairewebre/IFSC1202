def percentchange(t,y):
    change = ((t-y)/y) * 100
    return change
stockfile = open('06.02 Stock.txt', 'r')
stock = stockfile.readline()
print('{:10}{:10}'.format("Price","Change"))
print(stock)
