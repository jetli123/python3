# -*- coding: utf-8 -*-
"""git clone git://github.com/ansible/ansible.git --recursive"""
"""
# 1. wget https://mirrors.ustc.edu.cn/epel//7/x86_64/Packages/e/epel-release-7-11.noarch.rpm
# 2. rpm -ivh epel-release-7-11.noarch.rpm
# 3. rpm -ivh python-jinja2-2.7.2-2.el7.noarch.rpm --nodeps --安装依赖包
# 4. yum install ansible -y
"""

# Ansible 配置及测试
# vi /etc/ansible/hosts --添加两台主机IP
# 同时定义两个IP 到 webserver 组
"""
# Ex 1: Ungrouped hosts, specify before any group headers.

## green.example.com
## blue.example.com
192.168.10.172
192.168.10.145

# Ex 2: A collection of hosts belonging to the 'webservers' group

[webservers]
## alpha.example.org
## beta.example.org
192.168.10.172
192.168.10.145
"""
# 测试
"""
[root@kvm-server ~]# ansible webservers -m ping -k  --添加 -k 参数需要输入密码
SSH password:
192.168.10.172 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.10.145 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
"""

# 配置Linux 主机SSH 无密码访问
# 通过证书签名达到SSH 无密码。推荐使用 ssh-keygen 和 ssh-copy-id 来快速实现证书的生成及公钥下发。
# [root@kvm-server ~]# ssh-keygen -t rsa  下一步、下一步完成
# [root@kvm-server ~]# cd .ssh
# [root@kvm-server .ssh]# ls -l
# total 12
# -rw-------  1 root root 1679 Jan  5 12:14 id_rsa
# -rw-r--r--  1 root root  404 Jan  5 12:14 id_rsa.pub
# -rw-r--r--. 1 root root 1042 Jan  5 12:31 known_hosts
# [root@kvm-server .ssh]# pwd
# /root/.ssh
# [root@kvm-server .ssh]#
# [root@kvm-server .ssh]# ssh-copy-id -i id_rsa.pub root@192.168.10.145
# [root@kvm-server .ssh]# ssh-copy-id -i id_rsa.pub root@192.168.10.172
#
"""
[root@kvm-server ~]# ansible webservers -m ping
192.168.10.145 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.10.172 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
[root@kvm-server ~]#
"""
