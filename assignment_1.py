def sumIntervals(inp_list):
	countlist = []
	for sublist in inp_list:
		for i in range(sublist[0], (sublist[-1])):
			countlist.append(i)
	print len(set(countlist))