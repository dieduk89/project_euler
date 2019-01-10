
import math

print "\nCALCULUS\n"
	
def prime_factors(n):
	factors = [[2,0]]
	aux = n
	num = 2
	while num<aux**0.5:
		if aux%num==0:
			aux = aux/num
			if(factors[-1][0]==num):
				cant = factors[-1][1]
				factors[-1][1] = cant+1
			else:
				factors.append([num,1])
		else:
			num = num+1
	factors.append([aux,1])		
	return factors	

n = 600851475143	

print prime_factors(n)[-1][0]	

print "\n"
