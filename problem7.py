

def prime_factors (start,stop):
   numbers = list (range(start,stop+1))
   first_numbers = []
   for number in numbers:
      for x in range (2, number):
         if number % x == 0: 
          break
      else:
           first_numbers.append(number)
   if 1 in first_numbers:
     first_numbers.remove (1)    
   return (first_numbers)     

f = list (prime_factors (1,130000))
print (f[10000])
