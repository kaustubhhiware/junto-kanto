def main(n):
	p_dir = "part"+str(n)+"/"

	f = open(p_dir+"Step3/label_prop_output.txt",'r')
	f1 = open(p_dir+"gold_labels.txt",'r')
	s1 = f.read()
	s2 = f1.read()
	f.close()
	f1.close()

	s1 = s1.split("\n")
	s2 = s2.split("\n")

	tot = [0,0]

	dic = {}
	for each in s2:
		k = each.split("\t")
		if len(k) < 2:
			continue
		dic[k[0]] = k[1]
		if k[1] == "L1":
			tot[0] += 1
		elif k[1] == "L2":
			tot[1] += 1

	res = [0,0]

	for each in s1:
		k = each.split("\t")
		if len(k) < 2:
			continue
		if k[0] in dic:
			if k[1][0:2] == dic[k[0]]:
				if dic[k[0]] == "L1":
					res[0] += 1
				else:
					res[1] += 1

	print "total",tot
	print "result",res


main(15)
