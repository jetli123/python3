#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
import paramiko

hostname = "172.16.230.68"
username = "root"
password = "centos"
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get("/root/test.txt", r"C:\Users\JetLi\Desktop\test.txt")
    t.close()
except Exception as e:
    print(str(e))