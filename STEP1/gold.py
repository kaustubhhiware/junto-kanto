def main(n,label,count):
	f1 = open("part"+str(n)+"/seeds.txt",'r')
	text = f1.read()
	f1.close()
	data = text.split("\n")
	s_data = ""
	g_data = ""
	for each in data:
		if count>0:
			try:
				if each.split("\t")[1] == label:
					g_data+= (each)+'\n'
					count-=1
				else:
					s_data+= (each)+'\n'
			except IndexError:
				print "Error"
		else:
			s_data += each+'\n'

	f1 = open("part"+str(n)+"/seeds.txt",'wb')
	f1.write(s_data)
	f1.close()

	f1 = open("part"+str(n)+"/gold_labels.txt",'wb')
	f1.write(g_data)
	f1.close()

# main(4,"L1",7)
# main(7,"L1",87)
# main(26,"L1",52)
main(23,"L1",178)
# main(20,"L2",450)
