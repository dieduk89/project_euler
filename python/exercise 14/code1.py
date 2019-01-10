
print "\nSEEK RECURSIVE\n"

steps = [0 for x in range(10**6)]

for i in range(20):
	steps[2**i] = i

def collatz_check(n):
	s=0
	if n >= 10**6:
		while n>=10**6:
			s = s+1
			if n%2	== 0:
				n = n/2
			else:
				n = 3*n+1
	if steps[n] > 0:
			return s+steps[n]
	if n%2 == 0:
		steps[n] = 1+collatz_check(n/2)
	else:
		steps[n] = 1+collatz_check(3*n+1)
	return s+steps[n]	

for n in range(10**6-1,0,-1):
	if steps[n]==0:
		collatz_check(n)

max_steps  = max(steps)

print steps.index(max_steps)

print "\n"