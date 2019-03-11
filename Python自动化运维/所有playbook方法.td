(1)、shell
- name: shell module
  shell: if [ -z {{ ansible_distribution }} ];then exit 1; else echo {{ ansible_distribution_major_version }}; fi;
  register: command_result     # 输出到 command_result
  failed_when: command_result.stdout == ""   # 判断错误 key值 stdout 为空 判断为false
  # failed_when: "'failed' in command_result.stderr"
  # failed_when: result.rc == 1
  changed_when: False
  ignore_errors: True  # 忽略错误，即使有错误ignore（忽略）继续下一个 task执行。
- debug:
     msg: "{{ command_result.stdout }}"
     # msg: "{{ command_result.stdout_lines }}"
     # msg: "{{ command_result.stderr }}"
     # msg: "{{ command_result.rc }}"
  
- name: echo name info
  shell: if [ -z {{ name_a }} ];then exit 1; else echo {{ name_a }}; fi;
  register: result
  failed_when: result.rc == 1
  changed_when: result.rc == 0 or result.rc != 1
  debug:
     msg: "{{ result.stdout_line }}"


(2)、copy
- name: copy raid scripts
  copy: src={{ item }} dest=/tmp/ owner=zabbix group=zabbix mode=0755
  with_fileglob:
   - MegaRAID_*   # 去 file 目录去寻找 MegaRAID开头的文件

(3)、lineinfile
- name: write to file
  lineinfile:
   line: "zabbix\t\tALL=NOPASSWD:/opt/MegaRAID/storcli/storcli64"
   dest: /etc/sudoers.d/zabbix
   state: present
   create: yes

- name: set abc.txt
  lineinfile:
    line: "{{ item.line }}"
    dest: "{{ item.file }}"
    state: present
    create: yes
    regexp: "{{ item.regex }}"
  with_items:
    - { regex: "^1.*", line: "Hello World", file: "/tmp/abc.txt" }
    - { regex: "^2.*", line: "Hello Lilei", file: "/tmp/abc.txt" }
    - { regex: "^3.*", line: "Hello Luci", file: "/tmp/abc.txt" }
    
    
(4)、service
 - name: restart network
   service:
     name: network
     state: restarted
     enable: yes  # 添加到开机启动


(5)、yum
- name: install epel for CentOS 7
  yum: name={{ item }} state=present
  with_items:
    - '{{ url_7 }}'
    - '{{ url_rpm }}'

- name: install nc and netstat
  ignore_errors: True
  yum:
    name=['netstat']
    state=present
    download_only=yes
    update_cache=yes  # 重新刷 yum 缓存
    

(6)、authorized_key
- name: Adds an SSH authorized key
  authorized_key:
    user: root
    state: present
    key: "{{ lookup('file', '/root/.ssh/id_rsa.pub') }}"

- name: Adds an SSH authorized key
  authorized_key:
    user: root
    state: present
    key: "{{ lookup('file', lookup('env', 'HOME') + '/.ssh/id_rsa.pub') }}"


(7)、template
- name: template name
  template: src=resolv.conf dest=/tmp/resolv.conf
  

(8)、set_fact  # 可以夸多个 yml文件引用
- name: split str to template
  set_fact:
    IP: "{{ item.split(':')[1] }}"
  with_items: "{{ sids.split(',') }}"
  register: split_result

(9)、notify 
- name: config ssh server
  lineinfile:
    line: "PasswordAuthentication no"
    path: /etc/ssh/sshd_config
    regexp: "^PasswordAuthentication.*yes$"
    backrefs: yes
  notify: restart sshd  # 配置完文件 重启某服务，去handlers 目录中去寻找main.yml 文件中的 - name: restart sshd 的task

(10)、mate
- meta: flush_handlers  # 立即执行上面 handlers 目录中main.yml文件中的 - name: restart sshd 的task，
                        # 没有这个模块，默认等待这个 playbook执行完毕后在执行重启。
                        
(11)、cron
- name: creates an entry like "0 5,2 * * *"
  cron:
    name: "check dirs"
    minute: "*/10"
    job: "/usr/bin/ls -lrt /tmp >>/tmp/1.log 2>&1"
    cron_file: testops  # 在 /etc/cron.d/ 下创建文件 testops文件
    user: root

(12)、file
- name: create file
  file:
    path: /tmp/httpd.conf
    owner: root
    group: root
    mode: 0644
    state: touch

- name: recursively create dir
  file: state=directory recurse=yes path=/tmp/{{ item }}
  with_items:
    - back
    - temp
    - recycle
  changed_when: False

(13)、replace
- name: replace httpd.conf
  replace:
    path: "/tmp/httpd.conf"
    regexp: '(NameVirtualHost|Listen\s+)80'
    replace: '\1 127.0.0.1:8080'
    backup: yes

(14)、become_method
- name: test connect
shell: ls /
become: yes
remote_user: lilei
ignore_errors: True
become_method: sudo

(15)、tags  # ansible-playbook webservers -i test_hosts --tags=haha  指定这个tags haha标签的task 执行
- name: config 1.txt
  lineinfile:
  line: '{{ item }}'
  dest: /tmp/1.txt
  state: present
  create: yes
  ignore_errors: True
  register: command_config
  with_items:
     - 'ab - cd -aaa1'
     - 'cc - uw -kv23'
  tags: haha
 
 
(16)、user
- name: create user lilei
  user: name={{ item }} state=present
  with_items:
     - lilei
     - jetli

(17)、
 
