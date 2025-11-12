import math
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


biggest_tawan = []       
f = prime_factors (1,20)
for number in f:
   if number **4<20:
      biggest_tawan.append(number **4)
   elif number **3<20:
      biggest_tawan.append(number **3)
   elif number **2<20:
      biggest_tawan.append(number **2)
   elif number **1<20:
      biggest_tawan.append(number **1)
print (biggest_tawan)
x = math.prod(biggest_tawan)
print (x)