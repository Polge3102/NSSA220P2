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
    seq_num_list = []
    roundtrip_time = 0
    reply_delay = 0
    for i in L:
        if (i[1] == host_ip and i[5] == "Request"):
            requests_sent += 1
            requests_sent_bytes += i[4]
            requests_sent_data += (i[4] - 42)
            seq_num_list.append([i[0], i[6]])
        if (i[1] != host_ip and i[5] == "Request"):
            requests_received += 1
            requests_received_bytes += i[4]
            requests_received_data += (i[4] - 42)
        if (i[1] == host_ip and i[5] == "Reply"):
            replies_sent += 1
            for seq in seq_num_list:
                if (i[6] == seq[1]):
                    roundtrip_time += (i[0] - seq[0]) 
        if (i[1] != host_ip and i[5] == "Reply"):
            replies_received += 1        
    print(requests_sent, requests_received, replies_sent, replies_received, requests_sent_bytes, requests_received_bytes, requests_sent_data, requests_received_data, roundtrip_time)

L=[
[0.000000, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Request", "14/3584", 128],
[0.003678, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Reply", "14/3584", 126],
[1.204302, "192.168.100.1", "192.168.200.1", "ICMP", 74, "Request", "19/3584", 126],
[1.204322, "192.168.200.1", "192.168.100.1", "ICMP", 74, "Reply", "19/3584", 128]
]
host_ip = "192.168.200.1"
compute(L)
  
