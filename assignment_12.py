import string
with open (raw_input("Enter file name:"), "r") as in_file:
	letters = []
	nopunct = string.maketrans('''"',!?.;:()''', 10*" ")
	text = in_file.read().upper()
textv2 = text.translate(nopunct)
clean_text = textv2.split()
for line in clean_text:
	for char in line:
		letters.append(char)
total_letters = len(letters)
d= {}
for i in letters:
	d[i] = letters.count(i)
for key in d:
	d[key] = float(d[key])/total_letters
key_max = max(d.keys(), key=(lambda x: d[x]))
key_min = min(d.keys(), key=(lambda x: d[x]))
print key_max, key_min
text.replace(key_min, key_max)
print text