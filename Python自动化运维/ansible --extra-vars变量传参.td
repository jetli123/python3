命令行中传递变量:

一、除了`vars_prompt`和`vars_files`也可以通过Ansible命令行发送变量.如果你想编写一个通用的发布playbook时则特别有用,你可以传递应用的版本以便部署:

[root@s316-dal9 playbooks]# ansible-playbook release.yml --extra-vars "version=1.23.45 other_variable=foo"

其它场景中也很有用,比如为playbook设置主机群组或用户.

---

- hosts: '{{ hosts }}'
  remote_user: '{{ user }}'

  tasks:
     - ...

[root@s316-dal9 playbooks]# ansible-playbook release.yml --extra-vars "hosts=vipers user=starbuck"

二、Ansible 1.2中你也可以给extra-vars传递JSON,比如:

--extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'

key=value形式非常简单,但很实用!

Ansible 1.3中,实用”@”语法可以为extra-vars传递JSON文件:

--extra-vars "@some_file.json"
同样在Ansible 1.3中,我们可以为extra-vars传递YAML格式,无论直接通过命令行还是放置在文件中.
--extra-vars "@some_file.yml"

三、变量的优先级: 我该在什么地方放置变量?

如果同样名称的变量在多个地方都有定义,那么采纳是有个确定的顺序,如下:

* extra vars (-e in the command line) always win
* then comes connection variables defined in inventory (ansible_ssh_user, etc)
* then comes "most everything else" (command line switches, vars in play, included vars, role vars, etc)
* then comes the rest of the variables defined in inventory
* then comes facts discovered about a system
* then "role defaults", which are the most "defaulty" and lose in priority to everything.

* extra vars (在命令行中使用 -e)优先级最高
* 然后是在inventory中定义的连接变量(比如ansible_ssh_user)
* 接着是大多数的其它变量(命令行转换,play中的变量,included的变量,role中的变量等)
* 然后是在inventory定义的其它变量
* 然后是由系统发现的facts
* 然后是 "role默认变量", 这个是最默认的值,很容易丧失优先权

注：在1.5.4版本级以后,关于系统的自发现的facts也包含在大多数的其它变量中.

四、参数化roles

传给角色参数，覆盖默认值

roles:
   - { role: apache, http_port: 8080 }
   
 This makes it clear to the playbook reader that you’ve made a conscious choice to override some default in the role, 
 or pass in some configuration that the role can’t assume by itself. 
 It also allows you to pass something site-specific that isn’t really part of the role you are sharing with others.

This can often be used for things that might apply to some hosts multiple times, like so:  
roles:
   - { role: app_user, name: Ian    }
   - { role: app_user, name: Terry  }
   - { role: app_user, name: Graham }
   - { role: app_user, name: John   }

五、还有一些额外的事情与roles有关系

  一般来说，在一个角色中设置变量对其它角色可用。这意味着，如果有有 “roles/common/vars/main.yml” ，你可以在其中设置变量，
  并在你的剧本的其他角色和其他地方使用它们。
