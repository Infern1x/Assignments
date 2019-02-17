import math
firstnum = math.ceil(input("Enter the first number:"))
secondnum = math.floor(input("Enter the second number:"))
listofnums = [firstnum, secondnum]
diff = input("Enter an integer:")
downlimit= int (firstnum)
uplimit= int (secondnum + 1)
listofprimes = []
for i in range (downlimit, uplimit):
	if i <= 1:
		continue
	for k in range(2, i):
		if i%k == 0:
			break
	else: 
		listofprimes.append(i)
finished = False
for i in listofprimes:
	if finished == True:
		break
	for k in listofprimes:
		if (i-k) == diff:
			print "The first pair of primes that satisfies the condition is: [{},{}]".format(k,i)
			finished = True
