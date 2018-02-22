def main(n):
	f1 = open("/home/harsha/Tadditha/Changes/2_STEP/part"+str(n)+"/edge_weights.txt",'r')
	text = f1.read()
	f1.close()
	f2 = open("part"+str(n)+"/edge_weights.txt",'wb')
	f2.write(text)
	f2.close()

for i in range(1,31):
	if i in [5,10,12,18,22,24]:
			continue
	main(i)