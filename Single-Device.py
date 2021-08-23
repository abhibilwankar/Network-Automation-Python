from netmiko import ConnectHandler

r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

con = ConnectHandler(**r1)

##print(con.is_alive())

if con.is_alive():
    print(f'SSH Connection established with {con.host}')
    con.disconnect()
    if con.is_alive():
        print(f'SSH Connection is still alive with {con.host}')
    else:
        print(f'SSH Connection closed with node: {con.host} ...')

    
else:
    print('SSH Connection Failed ...')

