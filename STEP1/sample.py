def main():
	f = open("SL_preverbs.txt",'r')
	text = f.read()
	data = text.split("\n")
	lis = []
	for each in data:
		lis.append(each.split(" = ")[0])
	return lis