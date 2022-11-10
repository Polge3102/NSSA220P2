import sys
from urllib import request

def compute(L):
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
    for i in L:
        if (i[1] == host_ip and i[5] == "Request"):
            requests_sent += 1
            requests_sent_bytes += i[4]
            requests_sent_data += (i[4] - 42)
            rtt_seq_num_list.append([i[0], i[6], i[7]])
        if (i[1] != host_ip and i[5] == "Request"):
            requests_received += 1
            requests_received_bytes += i[4]
            requests_received_data += (i[4] - 42)
            rd_seq_num_list.append([i[0], i[6]])
        if (i[1] == host_ip and i[5] == "Reply"):
            replies_sent += 1
            for seq in rd_seq_num_list:
                if (i[6] == seq[1]):
                    reply_delay += (i[0] - seq[0])
                    rd_seq_num_list.remove(seq)   
        if (i[1] != host_ip and i[5] == "Reply"):
            replies_received += 1
            for seq in rtt_seq_num_list:
                if (i[6] == seq[1]):
                    roundtrip_time += (i[0] - seq[0])
                    total_hops += ((seq[2] - i[7])+ 1)
                    rtt_seq_num_list.remove(seq)

    avg_rtt = (roundtrip_time/requests_sent)
    throughput = ((requests_sent_bytes/1000)/roundtrip_time)
    goodput = ((requests_sent_data/1000)/roundtrip_time)
    delay = (reply_delay/requests_received)

    print("Echo Requests Sent: " + str(requests_sent))
    print("Echo Requests Received: " + str(requests_received))  
    print("Echo Replies Sent: " + str(replies_sent))  
    print("Echo Replies Received: " + str(replies_received))           
    print("Echo Request Bytes Sent (bytes): " + str(requests_sent_bytes))
    print("Echo Request Data Sent (bytes): " + str(requests_sent_data))
    print("Echo Request Bytes Received (bytes): " + str(requests_received_bytes))
    print("Echo Request Data Received (bytes): " + str(requests_received_data))

    print("Average RTT (milliseconds): " + str(avg_rtt * 1000))
    print("Echo Request Throughput (kB/sec): " + str(throughput))
    print("Echo Request Goodput (kB/sec): " + str(goodput))
    print("Average Reply Delay (microseconds): "+ str(delay * 1000000))
    print("Average Echo Request Hop Count: " + str(total_hops/requests_sent))

L=[
[0.000000, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Request", "14/3584", 128],
[0.003678, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Reply", "14/3584", 126],
[1.204302, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Request", "19/3584", 126],
[1.204322, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Reply", "19/3584", 128],
[1.500230, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Request", "23/3584", 128],
[1.510221, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Reply", "23/3584", 127],
[1.952140, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Request", "28/3584", 126],
[1.952145, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Reply", "28/3584", 128],
[2.001922, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Request", "34/3584", 128],
[2.005032, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Reply", "34/3584", 128],
[2.230000, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Request", "40/3584", 126],
[2.230005, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Reply", "40/3584", 128]
]
host_ip = "192.168.200.1"
compute(L)
  
