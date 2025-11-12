def Prime_factors (stop):
   prime_number = [2]
   for number in range (3,stop+1,2):
      is_prime = True
      sqr_number = int((number ** 0.5)+1)
      for x in prime_number:
         if x > sqr_number:
            break
         if number % x == 0: 
            is_prime = False
            break
      if is_prime:
         prime_number.append(number)
   
   return (prime_number) 

the_number = 600851475143
n = int((600851475143**0.5)+1)
prime_numbers = list (Prime_factors(n))

the_divisibles = []

for number in prime_numbers:
  if the_number % number == 0:
    the_divisibles.append (number)
print (max(the_divisibles))
    











































#range(2,13195)
#prime_numbers = [2,3,5]
#last_number = prime_numbers[-1]
#other_numbers = prime_numbers[:-1]
#results=[]
#for number in range(2,13195):
#    if 13195 % number == 0:
#        prime_numbers.append (number)
#        for item in prime_numbers:
#            if last_number % item == 0:
#                results.append (item)
                

    


#print(results)
#600851475143