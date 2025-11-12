#the 12th problem of Project Euler. solved: 4.jul.2025
import math
the_f = []
for number in range (2,102):
    x = number-1
    the_f.append(x)
r = (math.prod(the_f))

the_sep_number = []
for number in str(r):
    the_sep_number.append(int(number))
print (sum(the_sep_number))
