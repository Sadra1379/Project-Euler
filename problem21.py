#the 21th problem of Project Euler. solved: 4.jul.2025
def dev(number):
    numbers = []
    for i in range(1 , number):
        if number % i == 0: 
            numbers.append(i)
    total = sum(numbers)
    return(total)    

totall = []

for i in range (10000):
    new_number = dev(i)
    new_number2 = dev (new_number)
    if new_number == new_number2:
        continue
    if i == new_number2:
        totall.append(new_number2)

print(sum(totall))

        

    


