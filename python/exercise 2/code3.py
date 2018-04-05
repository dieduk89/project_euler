print "\nMATH EXPRESSION SIMPLIFIED\n"

gold_number = (1+5**0.5)/2

def get_fibonacci_number(index):
	return int(gold_number**(index+1)/5**0.5+0.5)

print sum([get_fibonacci_number(x) for x in range(2,33,3)])

print "\n"