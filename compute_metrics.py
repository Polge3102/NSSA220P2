requests_sent = 0
requests_received = 0
replies_sent = 0
replies_received = 0
requests_sent_bytes = 0
requests_received_bytes = 0
requests_sent_data = 0
requests_received_data = 0
rtt_seq_num_list = []
roundtrip_time = 0
rd_seq_num_list = []
reply_delay = 0
total_hops = 0

def rtt_compute(rtt_seq_num_list, i):
    global roundtrip_time
    global total_hops
    for seq in rtt_seq_num_list:
                if (i[5] == seq[1]):
                    roundtrip_time += (i[0] - seq[0])
                    total_hops += ((seq[2] - i[6])+ 1)
                    rtt_seq_num_list.remove(seq)

def rd_compute(rd_seq_num_list, i):
    global reply_delay
    for seq in rd_seq_num_list:
                if (i[5] == seq[1]):
                    reply_delay += (i[0] - seq[0])
                    rd_seq_num_list.remove(seq)   

def compute(packet_list, output_file, host_ip):
    global requests_sent
    global requests_sent_bytes
    global requests_sent_data
    global requests_received
    global requests_received_bytes
    global requests_received_data
    global replies_sent
    global replies_received

    for i in packet_list:
        if (i[1] == host_ip and i[4] == "request"):
            requests_sent += 1
            requests_sent_bytes += i[3]
            requests_sent_data += (i[3] - 42)
            rtt_seq_num_list.append([i[0], i[5], i[6]])
        elif (i[1] != host_ip and i[4] == "request"):
            requests_received += 1
            requests_received_bytes += i[3]
            requests_received_data += (i[3] - 42)
            rd_seq_num_list.append([i[0], i[5]])
        elif (i[1] == host_ip and i[4] == "reply"):
            replies_sent += 1
            rd_compute(rd_seq_num_list, i)
        else:
            replies_received += 1
            rtt_compute(rtt_seq_num_list, i)

    avg_rtt = (roundtrip_time/requests_sent)
    throughput = ((requests_sent_bytes/1000)/roundtrip_time)
    goodput = ((requests_sent_data/1000)/roundtrip_time)
    delay = (reply_delay/requests_received)

    output = open(output_file, "w")

    output.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received \n")
    output.write(str(requests_sent) + "," + str(requests_received) + "," + str(replies_sent) + "," + str(replies_received) + "\n")   
          
    output.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes) \n")
    output.write(str(requests_sent_bytes) + "," + str(requests_sent_data) + "\n")
    output.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes) \n")
    output.write(str(requests_received_bytes) + "," + str(requests_received_data) + "\n")

    output.write("Average RTT (milliseconds)," + str(round((avg_rtt * 1000), 2)) + "\n")
    output.write("Echo Request Throughput (kB/sec)," + str(round(throughput, 2)) + "\n")
    output.write("Echo Request Goodput (kB/sec)," + str(round(goodput, 2)) + "\n")
    output.write("Average Reply Delay (microseconds),"+ str(round((delay * 1000000), 2)) + "\n")
    output.write("Average Echo Request Hop Count," + str(round((total_hops/requests_sent), 2)) + "\n")

# Expecting a list of lists. Each list contains 7 values in a specific order. The time field to six decimal places, the source IP as a string, the destination IP as a string,
# the length of the frame as an int, whether it is a request or a reply as a string, the sequence number as a string (just the part before the slash), and the TTL as an int.
# L=[
# [0.000000, "192.168.200.1", "192.168.100.1", 74, "Request", "14", 128],
# [0.003678, "192.168.100.1", "192.168.200.1", 74, "Reply", "14", 126],
# [1.204302, "192.168.100.1", "192.168.200.1", 74, "Request", "19", 126],
# [1.204322, "192.168.200.1", "192.168.100.1", 74, "Reply", "19", 128],
# [1.500230, "192.168.200.1", "192.168.100.1", 74, "Request", "23", 128],
# [1.510221, "192.168.100.1", "192.168.200.1", 74, "Reply", "23", 127],
# [1.952140, "192.168.100.1", "192.168.200.1", 74, "Request", "28", 126],
# [1.952145, "192.168.200.1", "192.168.100.1", 74, "Reply", "28", 128],
# [2.001922, "192.168.200.1", "192.168.100.1", 74, "Request", "34", 128],
# [2.005032, "192.168.100.1", "192.168.200.1", 74, "Reply", "34", 128],
# [2.230000, "192.168.100.1", "192.168.200.1", 74, "Request", "40", 126],
# [2.230005, "192.168.200.1", "192.168.100.1", 74, "Reply", "40", 128]
# ]
# host_ip = "192.168.200.1"
# compute(L)
  
