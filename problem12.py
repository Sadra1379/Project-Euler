def first_factors (stop):
   numbers = list (range(3,stop+1,2))
   first_numbers = [2]
   for number in numbers:
        for x in first_numbers:
            if number % x == 0: 
                break
        else:
           first_numbers.append(number)
   
   return (first_numbers) 


i = 0
x = 0 
the_sum_list = []
the_list = []
while x < 500:
    i += 1
    the_divisors = []
    the_list.append (i)
    m = (sum(the_list))
    the_sum_list.append (m)
    for number in range (1,int(m**0.5)+1):
        if m % number == 0:
            the_other = m // number 
            if the_other == number:
                the_divisors.append (number)
            else:    
                the_divisors.append (number)
                the_divisors.append (the_other)
    x = (len(the_divisors))
     
            

print (m)