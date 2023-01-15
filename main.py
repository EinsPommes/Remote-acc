import paramiko

hostname = "hostname or ip"
username = "username"
password = "password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname, username=username, password=password)

stdin, stdout ,stderr = client.exec_command("command to execute")
output = stdin.read().decode("utf-8")

client.close()

print(output)