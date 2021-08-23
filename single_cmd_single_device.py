from netmiko import ConnectHandler

r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

con = ConnectHandler(**r1)

output = con.send_command('Show ip int b')
print(output)
