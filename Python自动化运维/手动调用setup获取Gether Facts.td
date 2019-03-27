ansible 通过 [Gather Facts] 这个默认任务收集远程主机的相关信息，包括（主机IP地址，主机名，系统半年报，硬件配置等信息）。
可以手动查看系统信息：利用 setup模块
指令： ansible localhost -m setup

官网说明：
ansible_facts
这个键应该包含一个字典，它将被附加到分配给主机的事实中。这些将是直接访问，不需要使用注册变量。
