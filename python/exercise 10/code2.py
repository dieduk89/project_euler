print "\nSEARCH OPTIMIZED\n"

def is_prime(primes,n):
	index = 0
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
		if is_prime(primes,num+2):
			primes.append(num+2)
		index = index+1
		num = 6*index-1
	return primes

primes = prime_list((2*10**6)**0.5+100)

val = sum(primes);

index = primes[-1]/6+2
num = 6*index-1

while num<2*10**6:
	if is_prime(primes,num):
		val = val+num
	if (num+2)<2*10**6:
		if	is_prime(primes,num+2):
			val = val+num+2
	index = index+1
	num = 6*index-1

print val

print "\n"



