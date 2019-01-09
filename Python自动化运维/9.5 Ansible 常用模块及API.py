# -*- coding: utf-8 -*-
# Ansible 提供了丰富的功能模块
# 1. Cloud（云计算）
# 2. Command（命令行）
# 3. Database（数据库）
# 4. Files（文件管理）
# 5. Internal（内置功能）
# 6. Inventory（资产管理）
# 7. Messaging（消息队列）
# 8. Monitoring（监控管理）
# 9. Net Infrastructure（网络基础服务）
# 10. Network（网络管理）
# 11. NOtification（通知管理）
# 12. Packageing（包管理）
# 13. Source Control（版本控制）
# 14. System（系统服务）
# 15. Utilities（公共服务）
# 16. Web Infrastructure（Web 基础服务）
""""""
# 更多查看官网 （http://ansibleworks.com/docs/modules.html）
"""
模块默认存储目录为 /usr/share/ansible/
# 存储结构：模块分类名作为目录名， 模块文件按分类存放在不同类别目录中。
# 命令行调用模块格式： ansible <pattren_goes_here（操作目标）> -m <module_name（模块名）> -a <module_args（模块参数）>
#
"""
# 默认模块为 -m command , 即“-m command ”可省略

# 获取远程webservers 组主机的 uptime信息
"""
[root@kvm-server ~]# ansible webservers -m command -a "uptime"
192.168.10.145 | CHANGED | rc=0 >>
 12:43:38 up 41 min,  2 users,  load average: 0.16, 0.05, 0.06

192.168.10.172 | CHANGED | rc=0 >>
 12:43:39 up 41 min,  2 users,  load average: 0.00, 0.01, 0.05

[root@kvm-server ~]# ansible webservers -m command -a "free -m"
192.168.10.145 | CHANGED | rc=0 >>
              total        used        free      shared  buff/cache   available
Mem:            991         102         766           6         123         743
Swap:           955           0         955

192.168.10.172 | CHANGED | rc=0 >>
              total        used        free      shared  buff/cache   available
Mem:            991         105         667           6         218         722
Swap:          1535           0        1535
"""
# 日常运维工作的常用模块

# 1.远程命令模块
# a.功能
# 包括： command、script、shell ，都可以实现远程shell命令运行。
# command : 作为 Ansible 的默认模块，可以运行远程权限规范所有的shell命令。
# script 功能：是在远程主机执行主控端存储的shell脚本文件，相当于 scp+shell 组合；
# shell 功能：是执行远程主机的shell脚本文件。

# b.例子
# ansible webservers -m command -a "free -m"
# ansible webservers -m script -a "/root/test.sh 12 34"
# ansible webservers -m shell -a "/tmp/test.sh 12"
"""
[root@kvm-server ~]# ansible webservers -m shell -a "/tmp/test.sh 12"
192.168.10.145 | CHANGED | rc=0 >>
success!

192.168.10.172 | CHANGED | rc=0 >>
success!

[root@kvm-server ~]#
"""

# 2.copy模块
# a.功能
# 实现主控端向目标主机拷贝文件，类似于scp 的功能。
# b.例子
# 拷贝/root/test.sh 文件至 webserver 组目标主机 /tmp/目录下，并更新文件属主及权限（可以单独使用file 模块实现权限的修改，
# 格式为：path=/etc/foo.conf owner=root group=root mode=0644）
"""
[root@kvm-server ~]# ansible webservers -m copy -a "src=/root/test.sh dest=/tmp/ owner=root group=root mode=0755"
192.168.10.145 | CHANGED => {
    "changed": true,
    "checksum": "559a56ae1d9c47c30e92db798d4610b8ca12b693",
    "dest": "/tmp/test.sh",
    "gid": 0,
    "group": "root",
    "md5sum": "33abc908e767e86c63754bee1e967161",
    "mode": "0755",
    "owner": "root",
    "secontext": "unconfined_u:object_r:admin_home_t:s0",
    "size": 123,
    "src": "/root/.ansible/tmp/ansible-tmp-1546665702.98-71589339895023/source",
    "state": "file",
    "uid": 0
}
192.168.10.172 | CHANGED => {
    "changed": true,
    "checksum": "559a56ae1d9c47c30e92db798d4610b8ca12b693",
    "dest": "/tmp/test.sh",
    "gid": 0,
    "group": "root",
    "md5sum": "33abc908e767e86c63754bee1e967161",
    "mode": "0755",
    "owner": "root",
    "secontext": "unconfined_u:object_r:admin_home_t:s0",
    "size": 123,
    "src": "/root/.ansible/tmp/ansible-tmp-1546665702.97-124778485558183/source",
    "state": "file",
    "uid": 0
}

"""

# 3.stat模块
# a.功能
# 获取远程文件状态信息，包括 atime、ctime、mtime、md5、uid、gid 等信息
# b.例子
"""
[root@kvm-server ~]# ansible webservers -m stat -a "path=/etc/sysctl.conf"
192.168.10.145 | SUCCESS => {
    "changed": false,
    "stat": {
        "atime": 1546597394.5445397,
        "attr_flags": "",
        "attributes": [],
        "block_size": 4096,
        "blocks": 8,
        "charset": "us-ascii",
        "checksum": "d599534a0fc9ac7757ed53aef73a9e39c90e49a3",
        "ctime": 1546595307.3558574,
        "dev": 64768,
        "device_type": 0,
        "executable": false,
        "exists": true,
        "gid": 0,
        "gr_name": "root",
        "inode": 8843807,
        "isblk": false,
        "ischr": false,
        "isdir": false,
        "isfifo": false,
        "isgid": false,
        "islnk": false,
        "isreg": true,
        "issock": false,
        "isuid": false,
        "mimetype": "text/plain",
        "mode": "0644",
        "mtime": 1523423393.0,
        "nlink": 1,
        "path": "/etc/sysctl.conf",
        "pw_name": "root",
        "readable": true,
        "rgrp": true,
        "roth": true,
        "rusr": true,
        "size": 449,
        "uid": 0,
        "version": "18446744072115391266",
        "wgrp": false,
        "woth": false,
        "writeable": true,
        "wusr": true,
        "xgrp": false,
        "xoth": false,
        "xusr": false
    }
}
192.168.10.172 | SUCCESS => {
    "changed": false,
    "stat": {
        "atime": 1546615245.5488045,
        "attr_flags": "",
        "attributes": [],
        "block_size": 4096,
        "blocks": 8,
        "charset": "us-ascii",
        "checksum": "d599534a0fc9ac7757ed53aef73a9e39c90e49a3",
        "ctime": 1546615038.9168046,
        "dev": 64768,
        "device_type": 0,
        "executable": false,
        "exists": true,
        "gid": 0,
        "gr_name": "root",
        "inode": 8726242,
        "isblk": false,
        "ischr": false,
        "isdir": false,
        "isfifo": false,
        "isgid": false,
        "islnk": false,
        "isreg": true,
        "issock": false,
        "isuid": false,
        "mimetype": "text/plain",
        "mode": "0644",
        "mtime": 1523423393.0,
        "nlink": 1,
        "path": "/etc/sysctl.conf",
        "pw_name": "root",
        "readable": true,
        "rgrp": true,
        "roth": true,
        "rusr": true,
        "size": 449,
        "uid": 0,
        "version": "18446744073290495865",
        "wgrp": false,
        "woth": false,
        "writeable": true,
        "wusr": true,
        "xgrp": false,
        "xoth": false,
        "xusr": false
    }
}
"""

# 4.get_url 模块
# a.功能
# 实现在远程主机下载指定URL到本地，支持 sha256sum 文件校验。
# b.例子
# ansible webservers -m get_url -a "url=http://www.baidu.com dest=/tmp/index.html mode=0440 force=yes"
"""
[root@kvm-server ~]# ansible webservers -m get_url -a "url=https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh dest=/tmp/"
192.168.10.208 | CHANGED => {
    "changed": true,
    "checksum_dest": null,
    "checksum_src": "698f35460634de156ed39b12d5aae2d9035ff4a9",
    "dest": "/tmp/shadowsocks.sh",
    "gid": 0,
    "group": "root",
    "md5sum": "4571cf3618564275c2c425b37f9f140b",
    "mode": "0644",
    "msg": "OK (13834 bytes)",
    "owner": "root",
    "secontext": "unconfined_u:object_r:admin_home_t:s0",
    "size": 13834,
    "src": "/root/.ansible/tmp/ansible-tmp-1546761083.04-60688306617466/tmpr5qlbb",
    "state": "file",
    "status_code": 200,
    "uid": 0,
    "url": "https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh"
}
192.168.10.172 | CHANGED => {
    "changed": true,
    "checksum_dest": null,
    "checksum_src": "698f35460634de156ed39b12d5aae2d9035ff4a9",
    "dest": "/tmp/shadowsocks.sh",
    "gid": 0,
    "group": "root",
    "md5sum": "4571cf3618564275c2c425b37f9f140b",
    "mode": "0644",
    "msg": "OK (13834 bytes)",
    "owner": "root",
    "secontext": "unconfined_u:object_r:admin_home_t:s0",
    "size": 13834,
    "src": "/root/.ansible/tmp/ansible-tmp-1546761082.99-169660863664474/tmpjTX3wi",
    "state": "file",
    "status_code": 200,
    "uid": 0,
    "url": "https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh"
}
192.168.10.145 | CHANGED => {
    "changed": true,
    "checksum_dest": null,
    "checksum_src": "698f35460634de156ed39b12d5aae2d9035ff4a9",
    "dest": "/tmp/shadowsocks.sh",
    "gid": 0,
    "group": "root",
    "md5sum": "4571cf3618564275c2c425b37f9f140b",
    "mode": "0644",
    "msg": "OK (13834 bytes)",
    "owner": "root",
    "secontext": "unconfined_u:object_r:admin_home_t:s0",
    "size": 13834,
    "src": "/root/.ansible/tmp/ansible-tmp-1546761083.03-98542564936660/tmp1yC8PP",
    "state": "file",
    "status_code": 200,
    "uid": 0,
    "url": "https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh"
}
"""
# 5. yum模块
# a.功能
# Linux平台软件包 管理操作，常见有 yum、apt 管理方式。
# b.例子
# ansible webservers -m apt -a "pkg=curl state=latest"
# ansible webservers -m yum -a "name=curl state=latest"
"""
[root@kvm-server ~]# ansible webservers -m yum -a "name=wget state=latest"
192.168.10.145 | SUCCESS => {
    "ansible_facts": {
        "pkg_mgr": "yum"
    },
    "changed": false,
    "msg": "",
    "rc": 0,
    "results": [
        "All packages providing wget are up to date",
        ""
    ]
}
192.168.10.208 | CHANGED => {
    "ansible_facts": {
        "pkg_mgr": "yum"
    },
    "changed": true,
    "msg": "",
    "obsoletes": {
        "grub2": {
            "dist": "x86_64",
            "repo": "@anaconda",
            "version": "1:2.02-0.65.el7.centos.2"
        },
        "grub2-tools": {
            "dist": "x86_64",
            "repo": "@anaconda",
            "version": "1:2.02-0.65.el7.centos.2"
        }
    },
    "rc": 0,
    "results": [
        "Loaded plugins: fastestmirror\n
        Loading mirror speeds from cached hostfile\n
         * base: mirrors.tuna.tsinghua.edu.cn\n
         * extras: mirrors.aliyun.com\n
         * updates: mirrors.aliyun.com\n
         Resolving Dependencies\n
         --> Running transaction check\n
         ---> Package wget.x86_64 0:1.14-18.el7 will be installed\n
         --> Finished Dependency Resolution\n\n

         Dependencies Resolved\n\n

         ================================================================================\n
         Package         Arch              Version                Repository       Size\n
         ================================================================================\n
         Installing:\n
         wget            x86_64            1.14-18.el7            base            547 k\n\n
         Transaction Summary\n
         ================================================================================\n
         Install  1 Package\n\n
         Total download size: 547 k\n
         Installed size: 2.0 M\n
         Downloading packages:\n
         Running transaction check\n
         Running transaction test\n
         Transaction test succeeded\n
         Running transaction\n
         Installing : wget-1.14-18.el7.x86_64                                      1/1 \n
         Verifying  : wget-1.14-18.el7.x86_64                                      1/1 \n\n
         Installed:\n  wget.x86_64 0:1.14-18.el7                                                     \n\n
         Complete!\n"
    ]
}
192.168.10.172 | SUCCESS => {
    "ansible_facts": {
        "pkg_mgr": "yum"
    },
    "changed": false,
    "msg": "",
    "rc": 0,
    "results": [
        "All packages providing wget are up to date",
        ""
    ]
}
"""

# 6.cron 模块
# a.功能
# 远程主机 crontab 配置。
# b.例子
# ansible webservers -m cron -a "name='check dirs' hour='5,2' job='ls -alh > dev/null'"

# 7.mount 模块
# a.功能
# 远程主机分区挂载。
# b.例子
# ansible webservers -m mount -a "name=/mnt/data src=/dev/sd0 fstype=ext3 opts=ro state=present"

# 8.service 模块
# a.功能
# 远程主机系统服务管理
# b.例子
# ansible webservers -m service -a "name=nginx state=stopped"
# ansible webservers -m service -a "name=nginx state=restarted"
# ansible webservers -m service -a "name=nginx state=reloaded"

# 9.sysctl 包管理模块
# a.功能
# 远程Linux主机 sysctl配置。
# b.例子
# sysctl: name=kernel.panic value=3 sysctl_file=/etc/sysctl.conf checks=before reload=yessalt '*' pkg.upgrade

# 10.user 服务模块
# a.功能
# 远程主机系统用户管理
# b.例子
# #添加用户 johnd;
# ansible webservers -m user -a "name=johnd comment='John Doe'"
# #删除用户 johnd;
# ansible webservers -m user -a "name=johnd state=absent remove=yes"
