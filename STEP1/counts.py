def main(n):
	f1 = open("part"+str(n)+"/seeds.txt",'r')
	text = f1.read()
	f1.close()
	data = text.split("\n")
	count_0 = 0
	count_1 = 0
	for each in data:
		try:
			if each.split("\t")[1] == "L2":
				count_1 += 1
			else:
				count_0 += 1
		except IndexError:
			print"IndexError"
	print "part"+str(n),count_0,count_1
for i in range(1,31):
	if i in [5,10,12,18,22,24]:
		continue
	main(i)