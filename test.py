#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
import paramiko

hostname = '192.168.1.213'
username = 'hadoop'
password = 'hadoop'
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(r'E:\各种软件\CentOS-7-x86_64-DVD-1804.iso', '/ISO/CentOS-7-x86_64-DVD-1804.iso')
    t.close()
except Exception as e:
    print(str(e))