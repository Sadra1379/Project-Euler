def multi (number,lastnumber):
    power = number**number
    new_power = str(power)
    last_10 = new_power[-10:]
    a = plus (last_10,lastnumber)
    return(a)
    

def plus (last_10,lastnumber):
    last_10 = int(last_10)
    new = last_10 + int(lastnumber)
    new_sum = str(new)
    the_new_10last = new_sum[-10:]
    return (the_new_10last)

number = 0 
for i in range (1000):
    number = multi(i,number)
number = int(number) -1
print(number)


        










