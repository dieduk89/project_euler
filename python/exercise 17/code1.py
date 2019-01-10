print "\nCALCULUS\n"

units = [
	'',
	'one', 
	'two' , 
	'three', 
	'four', 
	'five', 
	'six', 
	'seven', 
	'eight', 
	'nine', 
	'ten', 
	'eleven', 
	'twelve' , 
	'thirteen', 
	'fourteen', 
	'fifteen', 
	'sixteen', 
	'seventeen', 
	'eighteen', 
	'nineteen']

decs = [
	'twenty',
	'thirty',
	'forty',
	'fifty',
	'sixty',
	'seventy',
	'eighty',
	'ninety']

h100 = 'hundred'
t1000 = 'thousand'


sum_units = sum([len(units[x]) for x in range(10)])
sum_19 = sum([len(u) for u in units])
sum_decs = sum([len(d) for d in decs])

sum_99 = sum_19 + sum_decs * 10 + sum_units*len(decs)

print (sum_units + len(h100)*9) * 100 + sum_99 * 10 + len(units[1]) + len(t1000) + 3 *9 * 99

print "\n"