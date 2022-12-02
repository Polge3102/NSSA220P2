#NAME: Alex Polge
#DATE: 11-15-2022
#ASSIGNMENT: NSSA 220 - Project 2

#filename - filename as string of the document output from 'filter_packets.py'
#refrencelist - list passed by refrence that final output will be placed in
def parse(filename, refrencelist) :
	temp1 = list()
	temp2 = list()
	temp3 = list()
	line = ""

	print('called parse function in packet_parser.py')

	#Read threough file and store each frame as its own list
	#Each entry for frame is a line from said frame
	with open(filename) as f:
		for line in f:
			line = line.strip()

			#each frame is separated by a blank line, this restarts the line saving process
			if(line == ""):
				temp2.append(temp1)
				temp1 = list()
			#if line is not empty, save it in the list
			else:
				temp1.append(line)

	#frames are stored in a method that is earier to access
	#loop through all data. all data that is needed is stored in the first line
	#EX: ['1408', '1415.388433', '', '', '', '192.168.100.1', '', '', '', '', '', '', '', '', '192.168.100.2', '', '', '', '', '', '', '', '', 'ICMP', '', '', '', '', '942', '
	for x in temp2:
		#grab first line and get rid of empty strings
		temp3 = ' '.join(x[0].split(' ')).split()
		#store cleaned line for later use
		temp1 = list()

		#time field to six decimal places
		temp1.append(float(temp3[1]))

		#source IP as a string
		temp1.append(temp3[2])

		#destination IP as a string
		temp1.append(temp3[3])

		#length of the frame as an int
		temp1.append(int(temp3[5]))

		#whether it is a request or a reply as a string
		temp1.append(temp3[8])

		#sequence number as a string (just the part before the slash)
		temp1.append(temp3[10].split('=')[1].split('/')[0])

		#TTL as an int
		temp1.append(int(temp3[11].split('=')[1]))

		#save list in the refrencelist
		#EX: [590.404752, '192.168.100.1', '192.168.100.2', 74, 'request', '91', 128]
		refrencelist.append(temp1)

		#uncomment below for testing output
		#print(temp1)
