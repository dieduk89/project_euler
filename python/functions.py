

def is_prime(primes,n):
	index = 2
	result = True
	while primes[index]<= n**0.5 and result:
		result = n%primes[index] != 0
		index = index+1
	return result
		

def prime_list(limit):
	primes = [2,3,5,7]
	index = 2
	num = 6*index-1
	while num <= limit:
		if is_prime(primes,num):
			primes.append(num)
		if is_prime(primes,num+2) and (num+2)<limit:
			primes.append(num+2)
		index = index+1
		num = 6*index-1
	return primes

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

	def factorial(n):
	if n<2:
		return 1
	else:
		return n*factorial(n-1)
