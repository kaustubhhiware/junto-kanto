def main(n):
	f2 = open("STEP2/part"+str(n)+"/label_prop_output_step1.txt",'r')
	f4 = open("STEP3/part"+str(n)+"/label_prop_output_step1.txt",'wb')
	text = f2.read()
	f4.write(text)
	f2.close()
	f4.close()

	f2 = open("STEP2/part"+str(n)+"/label_prop_output_step2.txt",'r')
	f4 = open("STEP3/part"+str(n)+"/label_prop_output_step2.txt",'wb')
	text = f2.read()
	f4.write(text)
	f2.close()
	f4.close()
	
	data = text.split("\n")
	seeds_string = ""
	err_count = 0
	for each in data:
		print each
		if len(each.split("\t"))<2:
			print "Error"
			continue
		temp_s = each.split("\t")[0]
		temp_s += '\t'
		try:
			if each.split("\t")[1].split(" ")[1] == "1.0" or each.split("\t")[2].split(" ")[1] == "1.0":
				print "check"
				temp_s += each.split("\t")[1].split(" ")[0]+'\t'
				temp_s += each.split("\t")[1].split(" ")[1]+'\n'
			else:
				for i in range(5):
					if each.split("\t")[3].split(" ")[i] == "__DUMMY__":
						break
				j = 0
				check = 0
				while(j<5):
					if j==i:
						j+=2
						continue
					if check == 0:
						temp_s += each.split("\t")[3].split(" ")[j]+'\t'+each.split("\t")[3].split(" ")[j+1]+'\n'
						temp_s += each.split("\t")[0]
						temp_s += '\t'
						check = 1
					else:
						temp_s += each.split("\t")[3].split(" ")[j]+'\t'+each.split("\t")[3].split(" ")[j+1]+'\n'
					j+=2
		except IndexError:
			err_count +=1 
			continue
	
		seeds_string += temp_s

	f3 = open("STEP3/part"+str(n)+"/seeds.txt",'wb')
	print "part",str(n),"done"
	f3.write(seeds_string)
	f3.close()
	f= open("STEP2/part"+str(n)+"/gold_labels.txt",'r')
	text = f.read()
	f.close()
	f =open("STEP3/part"+str(n)+"/gold_labels.txt",'wb')
	f.write(text)

for i in range(2,3):
	if i in [5,10,12,18,22,24]:
		continue
	main(i)