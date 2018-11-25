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
    # sftp.get(r"/root/Desktop/kvm-create", r"C:\Users\JetLi\Desktop\kvm-create")  # 下载文件
    # sftp.mkdir("/home/userdir1", 0755)  # 创建目录
    # sftp.rmdir("/home/userdir1")  # 删除目录
    # sftp.rename("/homile.sh")  # 文件重命名
    # print sftp.stat("/root/sqe/test.sh", "/home/testflite3.py")  # 打印文件信息
    # print sftp.listdir("/home")  #/ 打印目录列表
    t.close()
except Exception as e:
    print(str(e))