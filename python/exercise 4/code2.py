print "\nBRUTE FORCE OPTIMIZED\n"

def is_palindrome(n):
	strn = list(str(n))
	revn = list(str(n))
	revn.reverse()
	return strn==revn

result = 0	

for x in range(900,1000):
	for y in range(x,1000):
		if is_palindrome(x*y) and x*y>result:
			result = x*y

print result

print "\n"