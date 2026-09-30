import math
S= 0
for n in range(1,51):
    S = S+ ((math.tan(2*n)/(math.factorial((2*n)+1)))*(math.log10(n+1)))
print(S)