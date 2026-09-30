import math
p= 1
for n in range(1,11):
    p=p*((((n**(n-1))+1)**0.5)/ ((math.log10((n**n)+1)**(1/3))*n**(n/3)))
print(p)
