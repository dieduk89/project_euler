
print "\nMATH ANALISYS\n"

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

def divisors(n):
	factors = prime_factors(n)
	result = 1
	for [p,exp] in factors:
		result = result*(exp+1)
	return result

index = 10
t_num = index*(index+1)/2

while divisors(t_num)<500:
	index = index+1
	t_num = index*(index+1)/2

print t_num

print "\n"