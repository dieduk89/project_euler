
print "\nCALCULUS EXTENSIVE\n"

def sumatory(total,step):
	end = int(total/step)
	return step*end*(end+1)/2

print sumatory(999,3) + sumatory(999,5) - sumatory(999,15)

print "\n"