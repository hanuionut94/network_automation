import getpass
import telnetlib

HOST = 'routers'
user = input('Enter your username: ')
password = getpass.getpass()

#f = open('routers')

with open('routers') as f:
	for IP in f:
		print(IP)
		IP = IP.strip()
		print(IP)
		print('Configuring echipment with IP: ' + (IP))
		tn = telnetlib.Telnet(IP)
		tn.read_until(b'Username: ')
		tn.write(user.encode('ascii') + b'\n')
		if password:
			tn.read_until(b'Password: ')
			tn.write(password.encode('ascii') + b'\n')
		tn.write(b'conf t \n')
		tn.write(b'int l3 \n')
		tn.write(b'ip add 3.3.3.3 255.255.255.255\n')
		tn.write(b'end\n')
		tn.write(b'quit\n')
		print(tn.read_all().decode('ascii'))	
