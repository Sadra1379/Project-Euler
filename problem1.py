#the first problem of Project Euler 21.jun.2025
numbers = []
for number in range (1,1000):
    if number % 3==0:
        numbers.append (number)
    if number % 5==0:
        if number in numbers:
            pass
        else:
            numbers.append (number)
print (sum(numbers))

