#the second problem of Project Euler 21.jun.2025
fibo =[1,2]
fibona =[1,2]
even_fibona=[]
r = 1
x = int()
while r<4000000:
    x= (fibo[0] + fibo[1])
    r= fibo[1]
    fibo.append (x)
    fibo.pop (0)
    fibona.append (x)
for x in fibona:
        if x % 2 == 0:
            even_fibona.append(x)
print (sum(even_fibona))
