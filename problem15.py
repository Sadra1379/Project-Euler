import math
def factoriel (stop):
    the_f = []
    for number in range (1,stop+1):
        the_f.append(number)
    r = (math.prod(the_f))
    return (r)


m = factoriel (20)
m_m = factoriel (40)
n = m_m / (m * m)
print (n)