Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from netmiko import ConnectHandler
>>> 
>>> 
>>> r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}
>>> 
>>> 
>>> con = ConnectHandler(r1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    con = ConnectHandler(r1)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\ssh_dispatcher.py", line 315, in ConnectHandler
    device_type = kwargs["device_type"]
KeyError: 'device_type'
>>> 
>>> con = ConnectHandler(**r1)
>>> 
>>> con
<netmiko.cisco.cisco_ios.CiscoIosSSH object at 0x000002260F6A7910>
>>> 
>>> con.is_alive()
True
>>> r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admi',
      'device_type': 'cisco_ios'}
>>> 
>>> con = ConnectHandler(**r1)
Traceback (most recent call last):
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 935, in establish_connection
    self.remote_conn_pre.connect(**ssh_connect_params)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\client.py", line 435, in connect
    self._auth(
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\client.py", line 764, in _auth
    raise saved_exception
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\client.py", line 751, in _auth
    self._transport.auth_password(username, password)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\transport.py", line 1509, in auth_password
    return self.auth_handler.wait_for_response(my_event)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\auth_handler.py", line 250, in wait_for_response
    raise e
paramiko.ssh_exception.AuthenticationException: Authentication failed.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    con = ConnectHandler(**r1)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\ssh_dispatcher.py", line 326, in ConnectHandler
    return ConnectionClass(*args, **kwargs)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\cisco\cisco_ios.py", line 17, in __init__
    return super().__init__(*args, **kwargs)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 350, in __init__
    self._open()
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 355, in _open
    self.establish_connection()
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 972, in establish_connection
    raise NetmikoAuthenticationException(msg)
netmiko.ssh_exception.NetmikoAuthenticationException: Authentication to device failed.

Common causes of this problem are:
1. Invalid username and password
2. Incorrect SSH-key file
3. Connecting to the wrong device

Device settings: cisco_ios 192.168.1.11:22


Authentication failed.
>>> r1 = {'host': '192.168.1.11',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}
>>> 
>>> 
>>> con = ConnectHandler(**r1)
>>> 
>>> 
>>> 
>>> con.is_alive()
True
>>> 
>>> r3 = {'host': '192.168.1.33',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}
>>> 
>>> con = ConnectHandler(**r3)
>>> 
>>> con.is_alive()
True
>>> 
>>> 
>>> 
>>> 
>>> r1['host']
'192.168.1.11'
>>> 
>>> 
>>> con.host
'192.168.1.33'
>>> 
>>> 
>>> 
>>> con.username
'admin'
>>> 
>>> 
>>> con.device_type
'cisco_ios'
>>> 
>>> con.password
'admin'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
True
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
SSH Connection established with 192.168.1.11
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
SSH Connection established with 192.168.1.11
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
SSH Connection established with 192.168.1.11
SSH Connection closed with node: 192.168.1.11 ...
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
SSH Connection closed with node: 192.168.1.77 ...
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
SSH Connection closed with node: 192.168.1.77 ...
SSH Connection closed with node: 192.168.1.77 ...
SSH Connection closed with node: 192.168.1.77 ...
SSH Connection closed with node: 192.168.1.77 ...
SSH Connection closed with node: 192.168.1.77 ...
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
Traceback (most recent call last):
  File "C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py", line 41, in <module>
    Node.disconnect()
AttributeError: 'dict' object has no attribute 'disconnect'
>>> type(Node)
<class 'dict'>
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
SSH Connection closed with node: 192.168.1.11 ...
SSH Connection closed with node: 192.168.1.33 ...
SSH Connection closed with node: 192.168.1.55 ...
SSH Connection closed with node: 192.168.1.66 ...
SSH Connection closed with node: 192.168.1.77 ...
>>> 
>>> 
>>> 
>>> con.check_enable_mode()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    con.check_enable_mode()
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\cisco_base_connection.py", line 14, in check_enable_mode
    return super().check_enable_mode(check_string=check_string)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 1654, in check_enable_mode
    self.write_channel(self.RETURN)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 459, in write_channel
    self._write_channel(out_data)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 417, in _write_channel
    self.remote_conn.sendall(write_bytes(out_data, encoding=self.encoding))
AttributeError: 'NoneType' object has no attribute 'sendall'
>>> 
>>> 
>>> con.is_alive()
False
>>> 
=============== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple-Devices.py ===============
SSH Connection established with 192.168.1.11
SSH Connection established with 192.168.1.33
SSH Connection established with 192.168.1.55
SSH Connection established with 192.168.1.66
SSH Connection established with 192.168.1.77
>>> 
>>> 
>>> con.is_alive()
True
>>> 
>>> 
>>> con.host
'192.168.1.77'
>>> 
>>> 
>>> 
>>> con.check_enable_mode()
True
>>> 
>>> 
>>> con.check_config_mode()
False
>>> 
>>> 
>>> con.check_config_mode()
False
>>> 
>>> 
>>> con.check_config_mode()
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> con.check_config_mode()
False
>>> 
>>> 
>>> con.check_enable_mode()
True
>>> 
>>> 
>>> con.disconnect()

>>> 
>>> 
>>> ConnectHandler(**r7)
<netmiko.cisco.cisco_ios.CiscoIosSSH object at 0x0000020F28738970>
>>> 
>>> 
>>> R7 = ConnectHandler(**r7)
>>> 
>>> 
>>> R7.is_alive()
True
>>> 
>>> 
>>> R7.check_config_mode()
False
>>> 
>>> 
>>> R7.config_mode()
'\r\nr7#configure terminal\r\n'
>>> 
>>> 
>>> R7.check_config_mode()
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> R7.check_enable_mode()
True
>>> 
>>> 
>>> 
>>> R7.keepalive
0
>>> 
>>> 
>>> 
>>> 
>>> help(R7.keepalive)

>>> 
>>> 
>>> 
================= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Single-Device.py ================
SSH Connection established with 192.168.1.11
SSH Connection closed with node: 192.168.1.11 ...
>>> 
>>> 
>>> con = ConnectHandler(**r1)
>>> 
>>> 
>>> con.is_alive()
True
>>> 
>>> 
>>> 
>>> con.send_command('show ip int b', '1.11')
'\nInterface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.11    YES manual up                    up      \nFastEthernet0/1            unassigned      YES unset  administratively down down    \nSerial1/0                  unassigned      YES unset  administratively down down    \nSerial1/1                  unassigned      YES unset  administratively down down    \nSerial1/2                  unassigned      YES unset  administratively down down    \nSerial1/3                  unassigned      YES unset  administratively down down    \nSerial1/4                  unassigned      YES unset  administratively down down    \nSerial1/5                  unassigned      YES unset  administratively down down    \nSerial1/6                  unassigned      YES unset  administratively down down    \nSerial1/7                  unassigned      YES unset  administratively down down    '
>>> 
>>> 
>>> print(con.send_command('show ip int b', '1.11'))
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
>>> 
>>> 
>>> print(con.send_command('show ip int b', '1.12'))
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    print(con.send_command('show ip int b', '1.12'))
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\utilities.py", line 500, in wrapper_decorator
    return func(self, *args, **kwargs)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 1535, in send_command
    raise IOError(
OSError: Search pattern never detected in send_command: 1.12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(con.send_command_timing('show ip int b', delay_factor = 2))
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    print(con.send_command_timing('show ip int b', delay_factor = 2))
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\utilities.py", line 500, in wrapper_decorator
    return func(self, *args, **kwargs)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 1297, in send_command_timing
    self.write_channel(command_string)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 459, in write_channel
    self._write_channel(out_data)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 417, in _write_channel
    self.remote_conn.sendall(write_bytes(out_data, encoding=self.encoding))
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\channel.py", line 846, in sendall
    sent = self.send(s)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\channel.py", line 801, in send
    return self._send(s, m)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\paramiko\channel.py", line 1198, in _send
    raise socket.error("Socket is closed")
OSError: Socket is closed
>>> con.keepalive(2)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    con.keepalive(2)
TypeError: 'int' object is not callable
>>> 
>>> con.is_alive()
False
>>> 
>>> 
>>> con.remote_conn
<paramiko.Channel 0 (closed) -> <paramiko.Transport at 0xcf12dc0 (unconnected)>>
>>> 
>>> con.remote_conn()
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    con.remote_conn()
TypeError: 'Channel' object is not callable
>>> 
>>> con.establish_connection()
''
>>> 
>>> 
>>> con.is_alive()
True
>>> 
>>> 
>>> con.keepalive(2)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    con.keepalive(2)
TypeError: 'int' object is not callable
>>> 
>>> 
>>> con.keepalive
0
>>> 
>>> 
>>> con.keepalive.__doc__
"int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
>>> 
>>> 
=========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_single_device.py ===========
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down    
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down    
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
>>> 
>>> 
>>> 
>>> type(output)
<class 'str'>
>>> 
>>> 
>>> output[0:]
'Interface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.77    YES manual up                    up      \nSerial0/0                  unassigned      YES unset  administratively down down    \nFastEthernet0/1            unassigned      YES unset  administratively down down    '
>>> 
>>> 
>>> print(output[0:])
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
>>> 
>>> 
>>> print(output[0:2])
In
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
**************************************************************************************************** 192.168.1.11 ****************************************************************************************************

Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
**************************************************************************************************** 192.168.1.33 ****************************************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
**************************************************************************************************** 192.168.1.55 ****************************************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down    
**************************************************************************************************** 192.168.1.66 ****************************************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down    
**************************************************************************************************** 192.168.1.77 ****************************************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
******************************************************************************** 192.168.1.11 ********************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
******************************************************************************** 192.168.1.33 ********************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
******************************************************************************** 192.168.1.55 ********************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down    
******************************************************************************** 192.168.1.66 ********************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down    
******************************************************************************** 192.168.1.77 ********************************************************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
**************************************** 192.168.1.11 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
**************************************** 192.168.1.33 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
**************************************** 192.168.1.55 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down    
**************************************** 192.168.1.66 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down    
**************************************** 192.168.1.77 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
**************************************** 192.168.1.11 ****************************************

Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
**************************************** 192.168.1.33 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
**************************************** 192.168.1.55 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down    
**************************************** 192.168.1.66 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down    
**************************************** 192.168.1.77 ****************************************
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
**************************************** 192.168.1.11 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
**************************************** 192.168.1.33 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
**************************************** 192.168.1.55 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down    
**************************************** 192.168.1.66 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down    
**************************************** 192.168.1.77 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
**************************************** 192.168.1.11 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down     

**************************************** 192.168.1.33 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down     

**************************************** 192.168.1.55 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down     

**************************************** 192.168.1.66 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down     

**************************************** 192.168.1.77 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down     

>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
**************************************** 192.168.1.11 ****************************************

 
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down     

**************************************** 192.168.1.33 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down     

**************************************** 192.168.1.55 ****************************************

 
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down     

**************************************** 192.168.1.66 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down     

**************************************** 192.168.1.77 ****************************************

 
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down     

>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py =========
Traceback (most recent call last):
  File "C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_cmd_multiple_devices.py", line 34, in <module>
    output = con.send_command('show ip int b', expect_string = '192.168.1.120')
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\utilities.py", line 500, in wrapper_decorator
    return func(self, *args, **kwargs)
  File "C:\Users\Abhinav\AppData\Local\Programs\Python\Python39\lib\site-packages\netmiko\base_connection.py", line 1535, in send_command
    raise IOError(
OSError: Search pattern never detected in send_command: 192.168.1.120
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw1              Fas 0/0            123         S I       WS-C3550- Fas 0/1
Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by Cisco Systems, Inc.
Compiled Thu 20-Jul-06 02:31 by prod_rel_team

ROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)

r1 uptime is 3 hours, 55 minutes
System returned to ROM by power-on
System image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2621XM (MPC860P) processor (revision 4.1) with 127102K/3970K bytes of memory.
Processor board ID FTX1050A1Q4
M860 processor: part number 5, mask 2
2 FastEthernet interfaces
8 Low-speed serial(sync/async) interfaces
32K bytes of NVRAM.
32768K bytes of processor board System flash (Read/Write)

Configuration register is 0x2142

>>> 
======== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_multiple_devices.py ========
Traceback (most recent call last):
  File "C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_multiple_devices.py", line 38, in <module>
    output = con.send_command(smd)
NameError: name 'smd' is not defined
>>> 
======== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_multiple_devices.py ========
**************************************** 192.168.1.11 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down     

**************************************** 192.168.1.11 ****************************************

 Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw1              Fas 0/0            133         S I       WS-C3550- Fas 0/1 

**************************************** 192.168.1.11 ****************************************

 Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by Cisco Systems, Inc.
Compiled Thu 20-Jul-06 02:31 by prod_rel_team

ROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)

r1 uptime is 3 hours, 58 minutes
System returned to ROM by power-on
System image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2621XM (MPC860P) processor (revision 4.1) with 127102K/3970K bytes of memory.
Processor board ID FTX1050A1Q4
M860 processor: part number 5, mask 2
2 FastEthernet interfaces
8 Low-speed serial(sync/async) interfaces
32K bytes of NVRAM.
32768K bytes of processor board System flash (Read/Write)

Configuration register is 0x2142
 

**************************************** 192.168.1.33 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.33    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES manual administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down     

**************************************** 192.168.1.33 ****************************************

 Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw3              Fas 0/0            151         S I       WS-C3750- Fas 1/0/3 

**************************************** 192.168.1.33 ****************************************

 Cisco IOS Software, 1841 Software (C1841-ADVENTERPRISEK9-M), Version 12.4(21), RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2008 by Cisco Systems, Inc.
Compiled Thu 10-Jul-08 00:00 by prod_rel_team

ROM: System Bootstrap, Version 12.4(13r)T5, RELEASE SOFTWARE (fc1)

r3 uptime is 4 hours, 2 minutes
System returned to ROM by power-on
System image file is "flash:c1841-adventerprisek9-mz.124-21.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 1841 (revision 7.0) with 352256K/40960K bytes of memory.
Processor board ID FTX12372072
2 FastEthernet interfaces
2 Serial(sync/async) interfaces
1 Virtual Private Network (VPN) Module
DRAM configuration is 64 bits wide with parity disabled.
191K bytes of NVRAM.
31488K bytes of ATA CompactFlash (Read/Write)

Configuration register is 0x2102
 

**************************************** 192.168.1.55 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.55    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
Serial0/1                  unassigned      YES unset  administratively down down    
Serial0/2                  unassigned      YES unset  administratively down down     

**************************************** 192.168.1.55 ****************************************

 Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw1              Fas 0/0            156         S I       WS-C3550-2Fas 0/5 

**************************************** 192.168.1.55 ****************************************

 Cisco IOS Software, C2600 Software (C2600-ADVIPSERVICESK9-M), Version 12.3(4)T6,  RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2004 by Cisco Systems, Inc.
Compiled Wed 05-May-04 21:46 by eaarmas

ROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)

R5 uptime is 3 hours, 59 minutes
System returned to ROM by power-on
System image file is "flash:c2600.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2610XM (MPC860P) processor (revision 0x400) with 126976K/4096K bytes of memory.
Processor board ID JHY0902K0ST (4218731053)
M860 processor: part number 5, mask 2
1 FastEthernet interface
1 Serial interface
2 Serial(sync/async) interfaces
32K bytes of NVRAM.
49152K bytes of processor board System flash (Read/Write)

Configuration register is 0x2102
 

**************************************** 192.168.1.66 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.66    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial0/0/0                unassigned      YES unset  administratively down down    
Serial0/0/1                unassigned      YES unset  administratively down down    
Serial0/1/0                unassigned      YES unset  administratively down down     

**************************************** 192.168.1.66 ****************************************

 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw2              Fas 0/0            169             S I   WS-C3550- Fas 0/6 

**************************************** 192.168.1.66 ****************************************

  

**************************************** 192.168.1.77 ****************************************

 Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.77    YES manual up                    up      
Serial0/0                  unassigned      YES unset  administratively down down    
FastEthernet0/1            unassigned      YES unset  administratively down down     

**************************************** 192.168.1.77 ****************************************

 Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw3              Fas 0/0            149         S I       WS-C3750- Fas 1/0/7 

**************************************** 192.168.1.77 ****************************************

 Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by Cisco Systems, Inc.
Compiled Thu 20-Jul-06 02:31 by prod_rel_team

ROM: System Bootstrap, Version 12.2(7r) [cmong 7r], RELEASE SOFTWARE (fc1)

r7 uptime is 3 hours, 58 minutes
System returned to ROM by power-on
System image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2621XM (MPC860P) processor (revision 1.0) with 127308K/3764K bytes of memory.
Processor board ID JAD06460LL9
M860 processor: part number 5, mask 2
2 FastEthernet interfaces
1 Serial interface
32K bytes of NVRAM.
32768K bytes of processor board System flash (Read/Write)

Configuration register is 0x2142
 

>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw1              Fas 0/0            140         S I       WS-C3550- Fas 0/1
Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by Cisco Systems, Inc.
Compiled Thu 20-Jul-06 02:31 by prod_rel_team

ROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)

r1 uptime is 4 hours, 2 minutes
System returned to ROM by power-on
System image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2621XM (MPC860P) processor (revision 4.1) with 127102K/3970K bytes of memory.
Processor board ID FTX1050A1Q4
M860 processor: part number 5, mask 2
2 FastEthernet interfaces
8 Low-speed serial(sync/async) interfaces
32K bytes of NVRAM.
32768K bytes of processor board System flash (Read/Write)

Configuration register is 0x2142

>>> 
>>> 
>>> 
>>> outputs
{'show ip int b': 'Interface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.11    YES manual up                    up      \nFastEthernet0/1            unassigned      YES unset  administratively down down    \nSerial1/0                  unassigned      YES unset  administratively down down    \nSerial1/1                  unassigned      YES unset  administratively down down    \nSerial1/2                  unassigned      YES unset  administratively down down    \nSerial1/3                  unassigned      YES unset  administratively down down    \nSerial1/4                  unassigned      YES unset  administratively down down    \nSerial1/5                  unassigned      YES unset  administratively down down    \nSerial1/6                  unassigned      YES unset  administratively down down    \nSerial1/7                  unassigned      YES unset  administratively down down    ', 'show cdp ne': 'Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n                  S - Switch, H - Host, I - IGMP, r - Repeater\n\nDevice ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\nSw1              Fas 0/0            140         S I       WS-C3550- Fas 0/1', 'show version': 'Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2006 by Cisco Systems, Inc.\nCompiled Thu 20-Jul-06 02:31 by prod_rel_team\n\nROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)\n\nr1 uptime is 4 hours, 2 minutes\nSystem returned to ROM by power-on\nSystem image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"\n\n\nThis product contains cryptographic features and is subject to United\nStates and local country laws governing import, export, transfer and\nuse. Delivery of Cisco cryptographic products does not imply\nthird-party authority to import, export, distribute or use encryption.\nImporters, exporters, distributors and users are responsible for\ncompliance with U.S. and local country laws. By using this product you\nagree to comply with applicable laws and regulations. If you are unable\nto comply with U.S. and local laws, return this product immediately.\n\nA summary of U.S. laws governing Cisco cryptographic products may be found at:\nhttp://www.cisco.com/wwl/export/crypto/tool/stqrg.html\n\nIf you require further assistance please contact us by sending email to\nexport@cisco.com.\n\nCisco 2621XM (MPC860P) processor (revision 4.1) with 127102K/3970K bytes of memory.\nProcessor board ID FTX1050A1Q4\nM860 processor: part number 5, mask 2\n2 FastEthernet interfaces\n8 Low-speed serial(sync/async) interfaces\n32K bytes of NVRAM.\n32768K bytes of processor board System flash (Read/Write)\n\nConfiguration register is 0x2142\n'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> outputs.keys()
dict_keys(['show ip int b', 'show cdp ne', 'show version'])
>>> 
>>> 
>>> 
>>> outputs.get('show ip int  b')
>>> 
>>> outputs.get('show ip int b')
'Interface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.11    YES manual up                    up      \nFastEthernet0/1            unassigned      YES unset  administratively down down    \nSerial1/0                  unassigned      YES unset  administratively down down    \nSerial1/1                  unassigned      YES unset  administratively down down    \nSerial1/2                  unassigned      YES unset  administratively down down    \nSerial1/3                  unassigned      YES unset  administratively down down    \nSerial1/4                  unassigned      YES unset  administratively down down    \nSerial1/5                  unassigned      YES unset  administratively down down    \nSerial1/6                  unassigned      YES unset  administratively down down    \nSerial1/7                  unassigned      YES unset  administratively down down    '
>>> 
>>> 
>>> 
>>> 
>>> print(outputs.get('show ip int b'))
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
>>> 
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========

Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw1              Fas 0/0            138         S I       WS-C3550- Fas 0/1
Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by Cisco Systems, Inc.
Compiled Thu 20-Jul-06 02:31 by prod_rel_team

ROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)

r1 uptime is 4 hours, 7 minutes
System returned to ROM by power-on
System image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2621XM (MPC860P) processor (revision 4.1) with 127102K/3970K bytes of memory.
Processor board ID FTX1050A1Q4
M860 processor: part number 5, mask 2
2 FastEthernet interfaces
8 Low-speed serial(sync/async) interfaces
32K bytes of NVRAM.
32768K bytes of processor board System flash (Read/Write)

Configuration register is 0x2142

>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
1 show ip int b
1 show cdp ne
1 show version
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
1 show ip int b
2 show cdp ne
3 show version
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 1
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
1 show ip int b
2 show cdp ne
3 show version
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 1
>>> 
>>> outputs.get(outputs.keys()[0])
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    outputs.get(outputs.keys()[0])
TypeError: 'dict_keys' object is not subscriptable
>>> 
>>> 
>>> outputs.get(outputs.keys())
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    outputs.get(outputs.keys())
TypeError: unhashable type: 'dict_keys'
>>> 
>>> 
>>> outputs.get()
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    outputs.get()
TypeError: get expected at least 1 argument, got 0
>>> 
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
1 show ip int b
2 show cdp ne
3 show version
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 1
>>> 
>>> 
>>> outputs
{'show ip int b': 'Interface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.11    YES manual up                    up      \nFastEthernet0/1            unassigned      YES unset  administratively down down    \nSerial1/0                  unassigned      YES unset  administratively down down    \nSerial1/1                  unassigned      YES unset  administratively down down    \nSerial1/2                  unassigned      YES unset  administratively down down    \nSerial1/3                  unassigned      YES unset  administratively down down    \nSerial1/4                  unassigned      YES unset  administratively down down    \nSerial1/5                  unassigned      YES unset  administratively down down    \nSerial1/6                  unassigned      YES unset  administratively down down    \nSerial1/7                  unassigned      YES unset  administratively down down    ', 'show cdp ne': 'Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n                  S - Switch, H - Host, I - IGMP, r - Repeater\n\nDevice ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\nSw1              Fas 0/0            129         S I       WS-C3550- Fas 0/1', 'show version': 'Cisco IOS Software, C2600 Software (C2600-ADVENTERPRISEK9-M), Version 12.4(8a), RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2006 by Cisco Systems, Inc.\nCompiled Thu 20-Jul-06 02:31 by prod_rel_team\n\nROM: System Bootstrap, Version 12.2(8r) [cmong 8r], RELEASE SOFTWARE (fc1)\n\nr1 uptime is 4 hours, 15 minutes\nSystem returned to ROM by power-on\nSystem image file is "flash:c2600-adventerprisek9-mz.124-8a.bin"\n\n\nThis product contains cryptographic features and is subject to United\nStates and local country laws governing import, export, transfer and\nuse. Delivery of Cisco cryptographic products does not imply\nthird-party authority to import, export, distribute or use encryption.\nImporters, exporters, distributors and users are responsible for\ncompliance with U.S. and local country laws. By using this product you\nagree to comply with applicable laws and regulations. If you are unable\nto comply with U.S. and local laws, return this product immediately.\n\nA summary of U.S. laws governing Cisco cryptographic products may be found at:\nhttp://www.cisco.com/wwl/export/crypto/tool/stqrg.html\n\nIf you require further assistance please contact us by sending email to\nexport@cisco.com.\n\nCisco 2621XM (MPC860P) processor (revision 4.1) with 127102K/3970K bytes of memory.\nProcessor board ID FTX1050A1Q4\nM860 processor: part number 5, mask 2\n2 FastEthernet interfaces\n8 Low-speed serial(sync/async) interfaces\n32K bytes of NVRAM.\n32768K bytes of processor board System flash (Read/Write)\n\nConfiguration register is 0x2142\n'}
>>> outputs.get(cmds[0])
'Interface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.11    YES manual up                    up      \nFastEthernet0/1            unassigned      YES unset  administratively down down    \nSerial1/0                  unassigned      YES unset  administratively down down    \nSerial1/1                  unassigned      YES unset  administratively down down    \nSerial1/2                  unassigned      YES unset  administratively down down    \nSerial1/3                  unassigned      YES unset  administratively down down    \nSerial1/4                  unassigned      YES unset  administratively down down    \nSerial1/5                  unassigned      YES unset  administratively down down    \nSerial1/6                  unassigned      YES unset  administratively down down    \nSerial1/7                  unassigned      YES unset  administratively down down    '
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
1 show ip int b
2 show cdp ne
3 show version
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 1

Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.1.11    YES manual up                    up      
FastEthernet0/1            unassigned      YES unset  administratively down down    
Serial1/0                  unassigned      YES unset  administratively down down    
Serial1/1                  unassigned      YES unset  administratively down down    
Serial1/2                  unassigned      YES unset  administratively down down    
Serial1/3                  unassigned      YES unset  administratively down down    
Serial1/4                  unassigned      YES unset  administratively down down    
Serial1/5                  unassigned      YES unset  administratively down down    
Serial1/6                  unassigned      YES unset  administratively down down    
Serial1/7                  unassigned      YES unset  administratively down down    
>>> 
========== RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/Multiple_cmds_single_device.py =========
1 show ip int b
2 show cdp ne
3 show version
SELECT NUMBER FROM 1-3 TO GET OUTPUT: 
 >>> 2
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Sw1              Fas 0/0            129         S I       WS-C3550- Fas 0/1
>>> 
>>> 
>>> outputs[cmd[0]]
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    outputs[cmd[0]]
KeyError: 's'
>>> outputs[cmds[0]]
'Interface                  IP-Address      OK? Method Status                Protocol\nFastEthernet0/0            192.168.1.11    YES manual up                    up      \nFastEthernet0/1            unassigned      YES unset  administratively down down    \nSerial1/0                  unassigned      YES unset  administratively down down    \nSerial1/1                  unassigned      YES unset  administratively down down    \nSerial1/2                  unassigned      YES unset  administratively down down    \nSerial1/3                  unassigned      YES unset  administratively down down    \nSerial1/4                  unassigned      YES unset  administratively down down    \nSerial1/5                  unassigned      YES unset  administratively down down    \nSerial1/6                  unassigned      YES unset  administratively down down    \nSerial1/7                  unassigned      YES unset  administratively down down    '
>>> 
============= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_device_config.py =============
>>> 
============= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_device_config.py =============
enter network to advertise: 192.168.1.0
Router 192.168.1.11 on wrong mode ...
>>> 
============= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_device_config.py =============
enter network to advertise: 192.168.1.0
router rip
r1(config-router)#network 192.168.1.0
r1(config-router)#no auto-summary
r1(config-router)#end
r1#
>>> 
============= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_device_config.py =============
enter network to advertise: 192.168.1.0
RIP has been configured on 192.168.1.11 !!!
>>> 
>>> 

>>> audit_rip
'Routing Protocol is "rip"\n  Outgoing update filter list for all interfaces is not set\n  Incoming update filter list for all interfaces is not set\n  Sending updates every 30 seconds, next due in 14 seconds\n  Invalid after 180 seconds, hold down 180, flushed after 240\n  Redistributing: rip\n  Default version control: send version 1, receive any version\n    Interface             Send  Recv  Triggered RIP  Key-chain\n    FastEthernet0/0       1     1 2                                  \n  Automatic network summarization is not in effect\n  Maximum path: 4\n  Routing for Networks:\n    192.168.1.0\n  Routing Information Sources:\n    Gateway         Distance      Last Update\n  Distance: (default is 120)\n'
>>> 
============= RESTART: C:/Users/Abhinav/Desktop/Python LABs/Study/VIT Morning/Day 6/single_device_config.py =============
enter network to advertise: 192.168.1.1
RIP configuration failed
>>> 
>>> 
>>> 
>>> rip_output
'router rip\nr1(config-router)#network 192.168.1.1\nr1(config-router)#no auto-summary\nr1(config-router)#end\nr1#'
>>> 
>>> 
>>> print(rip_output)
router rip
r1(config-router)#network 192.168.1.1
r1(config-router)#no auto-summary
r1(config-router)#end
r1#
>>> 
>>> 

>>> audit_rip
'Routing Protocol is "rip"\n  Outgoing update filter list for all interfaces is not set\n  Incoming update filter list for all interfaces is not set\n  Sending updates every 30 seconds, next due in 2 seconds\n  Invalid after 180 seconds, hold down 180, flushed after 240\n  Redistributing: rip\n  Default version control: send version 1, receive any version\n    Interface             Send  Recv  Triggered RIP  Key-chain\n    FastEthernet0/0       1     1 2                                  \n  Automatic network summarization is not in effect\n  Maximum path: 4\n  Routing for Networks:\n    192.168.1.0\n  Routing Information Sources:\n    Gateway         Distance      Last Update\n  Distance: (default is 120)\n'
>>> 
>>> 
>>> print(audit_rip)
Routing Protocol is "rip"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Sending updates every 30 seconds, next due in 2 seconds
  Invalid after 180 seconds, hold down 180, flushed after 240
  Redistributing: rip
  Default version control: send version 1, receive any version
    Interface             Send  Recv  Triggered RIP  Key-chain
    FastEthernet0/0       1     1 2                                  
  Automatic network summarization is not in effect
  Maximum path: 4
  Routing for Networks:
    192.168.1.0
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 120)

>>> con.is_alive()
True
>>> 
>>> 
>>> 
>>> help(con.establish_connection)
Help on method establish_connection in module netmiko.base_connection:

establish_connection(width=511, height=1000) method of netmiko.cisco.cisco_ios.CiscoIosSSH instance
    Establish SSH connection to the network device
    
    Timeout will generate a NetmikoTimeoutException
    Authentication failure will generate a NetmikoAuthenticationException
    
    :param width: Specified width of the VT100 terminal window (default: 511)
    :type width: int
    
    :param height: Specified height of the VT100 terminal window (default: 1000)
    :type height: int

>>> 
>>> 
>>> con.disconnect()
>>> 
>>> 
>>> 
>>> 
>>> con.is_alive()
False
>>> 
>>> 
>>> 
>>> con.establish_connection()
''
>>> con.is_alive()
True
>>> 
>>> 
>>> con.disconnect()

>>> 
>>> 
>>> 
>>> con.keepalive()
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    con.keepalive()
TypeError: 'int' object is not callable
>>> 
>>> con.keepalive
0
>>> 
>>> 
>>> 
>>> help(ConnectHandler)
Help on function ConnectHandler in module netmiko.ssh_dispatcher:

ConnectHandler(*args, **kwargs)
    Factory function selects the proper class and creates object based on device_type.

>>> 
>>> 
>>> ConnectHandler.__doc__
'Factory function selects the proper class and creates object based on device_type.'
>>> 
>>> 
>>> 
>>> 