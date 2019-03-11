(1)、shell
- name: shell module
  shell: if [ -z {{ ansible_distribution }} ];then exit 1; else echo {{ ansible_distribution_major_version }}; fi;
  register: command_result     # 输出到 command_result
  failed_when: command_result.stdout == ""   # 判断错误 key值 stdout 为空 判断为false
  # failed_when: "'failed' in command_result.stderr"
  # failed_when: result.rc == 1
  changed_when: False
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
   - MegaRAID_*

(3)、lineinfile
- name: write to file
  lineinfile:
   line: "zabbix\t\tALL=NOPASSWD:/opt/MegaRAID/storcli/storcli64"
   dest: /etc/sudoers.d/zabbix
   state: present
   create: yes
