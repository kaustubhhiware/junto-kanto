import random

def main(n,l1range,l2range,l1gold,l2gold):
	f = open("part"+str(n)+"/seeds.txt",'r')
	string = f.read()
	f.close()

	string = string.split("\n")
	seedout = ""
	excessout = ""
	goldout = ""
	for each in string:
		if(len(each.split("\t")) < 2):
			print "see"
			continue
		if each.split("\t")[1] == "L1":
			x = random.randrange(0,l1range)
			if x < l1gold:
				excessout += each + "\n"
			else:
				seedout += each + "\n"
		else:
			x = random.randrange(0,l2range)
			if x < l2gold:
				excessout += each + "\n"
			else:
				seedout += each + "\n"
			# seedout += each + "\n"

	f = open("part"+str(n)+"/seeds.txt",'wb')
	f.write(seedout)
	f.close()

	f = open("part"+str(n)+"/gold_labels.txt",'wb')
	f.write(excessout)
	f.close()

main(2,75,173,20,118)