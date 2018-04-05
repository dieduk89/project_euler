
print "\nMATH EXPRESSION\n"

gold_number = (1+5**0.5)/2

def get_fibonacci_number(index):
	return int(gold_number**(index+1)/5**0.5+0.5)

fibonacci = [get_fibonacci_number(x) for x in range(33)]

print sum([x for x in fibonacci if x%2==0])

print "\n"