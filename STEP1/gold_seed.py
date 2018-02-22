def main(n):
	f = open("part"+str(n)+"/seeds.txt",'r')
	seeds_text = f.read()
	f.close()
	try:
		f = open("part"+str(n)+"/gold_labels.txt",'r')
		gold_text = f.read()
		f.close()
	except IOError:
		gold_text = ""
	data_1 = []
	data_2 = []
	gold_data = gold_text.split("\n")
	seeds_data = seeds_text.split("\n")
	