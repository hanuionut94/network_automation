import paramiko
import getpass

username=input('Username: ')
password=getpass.getpass()

with open('routers') as f:
	for IP in f:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client(IP,port=22, username=username, password=password)

		stdin, stdout, stderr = ssh_client.exec_command('show version')
		output=stdout.read().decode()
		print(output)
		
		if ssh is not None:
			ssh_client.close()
			del client, stdin, stdout, stderr
		with open(IP + '_output.txt', 'w') as f:
			f.write(output)
	
