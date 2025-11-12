import time

def first_factors (stop):
   first_numbers = [2]
   for number in range (3,stop+1,2):
      is_prime = True
      sqr_number = int((number ** 0.5)+1)
      for x in first_numbers:
         if x > sqr_number:
            break
         if number % x == 0: 
            is_prime = False
            break
      if is_prime:
         first_numbers.append(number)
   
   return (first_numbers) 


start = time.time()
f = list (first_factors (2000000))
print (sum(f))
print (time.time()-start)