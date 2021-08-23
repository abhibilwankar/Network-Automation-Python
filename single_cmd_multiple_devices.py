from netmiko import ConnectHandler

r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

r3 = {'host': '192.168.1.33',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

r5 = {'host': '192.168.1.55',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

r6 = {'host': '192.168.1.66',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

r7 = {'host': '192.168.1.77',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

nodes = [r1, r3, r5, r6, r7]

for node in nodes:
    con = ConnectHandler(**node)

    if con.is_alive():
        output = con.send_command('show ip int b')
        ptrn = '*' * 40
        print(ptrn, con.host, ptrn)
        print ('\n',output,'\n')







