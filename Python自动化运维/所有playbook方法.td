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
    regexp: '^(NameVirtualHost|Listen\s+)80'
    replace: '\1 127.0.0.1:8080'
    backup: yes

- name: replace test 
  replace:
    path: /root/2.txt
    regexp: '(<name>)COK1(<name>.*)'
    replace: '\1COK2\2'

- name: replace 2
  replace:
    path: /root/2.txt
    regexp: '(-Djava.rmi.server.hostname)=.+?\s+.*'
    replace: '\1={{ inventory_hostname }}'


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

(17)、loop 循环字典 dict
- name: replace 3
  debug:
   # msg: "{{ item.0 }} {{ item.1 }}" # -->3
    msg: "{{ item.key }} {{ item.value }}" # --> 1,2,4
  loop: "{{ sidlist|dict2items }}" # 2
   # loop: "{{ sidlist|dictsort }}" # 3
   # loop: "{{ lookup ('dict', sidlist) }}" # 4

(18)、with_dict
- name: replace port info
  replace:
    path: /root/1.txt
    regexp: "{{ item.a }}"
    replace: "{{ item.b }}"
    # regexp: '(userId=)+tm'
    # replace: '\1cm'
  with_dict: 
    - "{{ sids }}"
    # - {'a': '^(redis.port)=.*', 'b': '\1={{ sids.value.port }}'}
    # - {'a': '(<property) (name="registryPort") value=".*?"/>', 'b': '\1 \2 value="{{ sids.value.port }}"/>'}

(19)、loop 循环 list 
- name: list 
  debug:
     msg: "{{ item }}"
  loop:
     - name
     - age
     - score    

(20)、with_list
- name: list 
  debug:
     msg: "{{ item }}"
  with_list:
     - name
     - age
     - score
     
 

     
(21)、with_items
- name: items
  debug:
     msg: "{{ item }}"
  with_items:
     - ['a', 'b', 'c']
 

(22)、with_indexed_items
- name: with_indexed_items
  debug:
    msg: "{{ item.0 }} - {{ item.1 }}"
  with_indexed_items: 
    - ['A', 'B', 'C']

(23)、loop (with_items)循环
- name: with_items -> loop
  debug:
    msg: "{{ item }}"
  loop: "{{ items|flatten(levels=1) }}"
  
(24)、loop (with_indexed_items)
- name: with_indexed_items -> loop
  debug:
    msg: "{{ index }} - {{ item }}"
  loop: "{{ items|flatten(levels=1) }}"
  loop_control:
    index_var: index
    
(25)、pause 暂停 时间
- name: test 1
  pause:
    seconds: 10
  delegate_to: localhost


(26)、vars_prompt # 手动输入参数
vars_prompt:
    - name: 'a'
      prompt: "Please input "
      private: no

(27)、with_nested # 嵌套循环
- name: give users access to multiple databases
  mysql_user: name={{ item[0] }} priv={{ item[1] }}.*:ALL append_privs=yes password=foo
  with_nested:
    - [ 'alice', 'bob' ]
    - [ 'clientdb', 'employeedb', 'providerdb' ]

item[0]是循环的第一个列表的值['alice','bob']。item[1]是第二个列表的值。表示循环创建alice和bob两个用户，并且为其赋予在三个数据库上的所有权限。
也可以将用户列表事先赋值给一个变量：

- name: here, 'users' contains the above list of employees
  mysql_user: name={{ item[0] }} priv={{ item[1] }}.*:ALL append_privs=yes password=foo
  with_nested:
    - "{{users}}"
    - [ 'clientdb', 'employeedb', 'providerdb' ]

(28)、with_fileglob # 列出与模式匹配的文件
- name: copy ganglia script
  copy: src={{ item }} dest=/usr/lib64/ganglia/ owner=root mode=755
  with_fileglob:
    - gmetric-*
