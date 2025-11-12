sumlist = []
for number in range (1,101):
    x = number **2
    sumlist.append(x)
print (sum(sumlist))

sumof100 = sum(range(1,101))
sqr = sumof100**2
print (sqr)
x = (sqr-sum(sumlist))
print (x)