
print "\nCALCULUS EXTENSIVE\n"

fibonacci = [1,1]

def fill_fibonacci(limit):
	new = fibonacci[-2]+fibonacci[-1]
	while new<limit:
		fibonacci.append(new)
		new = fibonacci[-2]+fibonacci[-1]

fill_fibonacci(4*10**6)

print sum([x for x in fibonacci if x%2==0])

print "\n"