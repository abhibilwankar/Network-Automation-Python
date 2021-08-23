from netmiko import ConnectHandler

network = input('enter network to advertise: ')

r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios',
      'keepalive': None}

con = ConnectHandler(**r1)


if con.is_alive():
    con.config_mode()
    if con.check_config_mode():
        rip = ['router rip',
               f'network {network}',
               'no auto-summary']
        
        rip_output = con.send_config_set(rip)
##        print(rip_output)
        audit_rip = con.send_command('show ip protocol')

        if 'rip' in audit_rip:
            print(f'RIP has been configured on {con.host} !!!')
        else:
            print('RIP configuration failed')
            
    else:

        print(f'Router {con.host} on wrong mode ...')

con.disconnect()
else:
    print('SSH is failed ...' )
