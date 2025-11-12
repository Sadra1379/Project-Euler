a = 1
kol = []
for i in range(1,1001):
    for j in range(4):
        a = a + (i*2)
        kol.append(a)
    if (i*2)+1 == 1001:
        break
    

print(sum(kol)+1)


