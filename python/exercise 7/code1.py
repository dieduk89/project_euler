print "\nSECUENCIAL SEARCH\n"

def is_prime(primes,n):
	index = 2
	result = True
	while primes[index]<= int(n**0.5) and result:
		result = n%primes[index] != 0
		index = index+1
	return result


primes = [2,3,5,7]
index = 2
num = 6*index-1
while len(primes)<10001:
	if is_prime(primes,num):
		primes.append(num)
	if is_prime(primes,num+2):
		primes.append(num+2)
	index = index+1
	num = 6*index-1

print primes[10000]

print "\n"