def fibonacci (stop):
    fibo = [1,1]
    f = 2
    while f < stop:
        f +=1
        x  = (fibo [-1] + fibo[-2])
        fibo.append (x)
    return (fibo)

x = 0 
f_index = 0
while x < 1000:
    f_index  += 1
    the_fibo = fibonacci (f_index)
    the_last = str(the_fibo [-1])
    x = len(the_last)
print (f_index)
