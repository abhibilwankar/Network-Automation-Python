from netmiko import ConnectHandler


r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

con = ConnectHandler(**r1)

cmds = ['show ip int b',
        'show cdp ne',
        'show version']

outputs = {'show ip int b': None,
           'show cdp ne': None,
           'show version': None}


           
for cmd in cmds:
    outputs[cmd] = con.send_command(cmd)
##    print(outputs.get(cmd))

n = 1
for k in outputs.keys():
    print(n,k)
    n += 1
    
print('select number from 1-3 to get output: '.upper())

usr_data = int(input(' >>> '))




if usr_data == 1:
    print(outputs.get(cmds[0]))

elif usr_data == 2:
    print(outputs.get(cmds[1]))

else:
    print(outputs.get(cmds[-1]))
