
print "\nMATH ANALISYS\n"

def get_b(a):
	return (500000.0-1000.0*a)/(1000.0-a)

a = 1
b = get_b(a)
while b-int(b)>0:
	a = a+1
	b = get_b(a)

c = 1000-a-b;

print int(a*b*c)

print "\n"