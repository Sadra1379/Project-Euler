#the 4th problem of Project Euler 24.jun.2025
all_numbers = []
palindroms = []
first = []
second = []
for first_number in range (100,1000):
    for second_number in range (100,1000):
        x = first_number*second_number
        all_numbers.append (x)
        a = str(x)
        if a == a [::-1]:
            A = int (a)
            palindroms.append (A)

print (max(palindroms))


