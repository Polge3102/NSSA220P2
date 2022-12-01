def filter(nodeFilename, outputFilename) :
	print('called filter function in filter_packets.py')
	captures = open(nodeFilename, 'r')
	filtered = open(outputFilename, 'w')
	line = captures.readline()
	while line:
		line = captures.readline()
		if line.count('Echo') >= 1:
			captures.readline()
			while line.count('0') >= 1:
				filtered.write(line)
				line = captures.readline()
				
		
	captures.close()
	filtered.close()
