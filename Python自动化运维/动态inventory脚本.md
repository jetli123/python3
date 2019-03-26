#!/usr/bin/env python
# -*- coding: utf8 -*-

import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import mysql.connector

try:
    import json
except ImportError:
    import simplejson as json
test = [
(115,8050),
(134,8103),
(234,8907),
(345,8317)
]


class Inventory(object):
    
    def __init__(self):
        self.migrate_id = []
        self.read_cli_args()
        self.and_zone = []
        self.inventory = {}
        self.hosts_dicts = {}
        self.metas_dicts = {}
        self.group_vars_dict = {}
        self.group_hosts_dict = []
        self.from_ip = []
        self.from_sid = ""
        self.from_redis_instance = ""
        self.to_sid = ""
        self.to_ip = ""
        if self.args.list:
            self.db_info()

        # Called with `--host [hostname]`
        elif self.args.host:
            # Not implemented, since we return `__meta` key for `--list` call
            self.inventory = self.empty_inventory()

        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory);

 


    def db_info(self):
        point = 0
        group_hosts_dict = []
        vars_dict = {}
        all_sid = []
        from_all_sid = []
        to_all_sid = []
        try:
            conn = mysql.connector.connect(user='root', password='mysql', host='localhost', database='im30', port='3306')
            cursor = conn.cursor()
            for i in test:
                ###
                host_vars = {}
                source_vars = {}
                to_SID = []
                from_sid = []
                from_redis_instance = []
                from_redis_instance2 = []
                to_sid = []
                to_ip = []
                ###
                cursor.execute("select zone, ip_inner, redis_instance from tbl_webserver where svr_name like '%%s%'", [i[0]])
                var_ = cursor.fetchone()
                ###
                self.from_sid = str(var_[0][3:])
                self.from_ip = str(var_[1])
                self.from_redis_instance = str(var_[2])
                cursor.execute("select zone, ip_inner from tbl_webserver where svr_name like '%%s%'", [i[1]])
                var__ = cursor.fetchone()
                self.to_sid = str(var__[0][3:])
                self.to_ip = str(var__[1])
                ###
                for k,v in self.hosts_dicts.items():
                    if self.from_ip == k:
                        self.hosts_dicts[k]["from_sid"].append(self.from_sid)
                        self.hosts_dicts[k]["from_redis_instance"].append(self.from_redis_instance)
                        self.hosts_dicts[k]["to_sid"].append(self.to_sid)
                        self.hosts_dicts[k]["to_ip"].append(self.to_ip)
                        point = 1
                    #else:
                    #    point = 0
                ###

                if point == 1:
                    pass
                elif point == 0:
                    from_sid.append(self.from_sid)
                    from_redis_instance.append(self.from_redis_instance)
                    to_sid.append(self.to_sid)
                    to_ip.append(self.to_ip)
                    host_vars["from_sid"] = from_sid
                    host_vars["from_redis_instance"] = from_redis_instance
                    host_vars["to_sid"] = to_sid
                    host_vars["to_ip"] = to_ip
                    self.hosts_dicts[self.from_ip] = host_vars
                point = 0
                for k,v in self.hosts_dicts.items():
                    if self.to_ip == k:
                        self.hosts_dicts[k]["from_redis_instance"].append(self.from_redis_instance)
                        self.hosts_dicts[k]["to_sid"] = self.to_sid
                        point = 1
                    #else:
                    #    point = 0
                if point == 1:
                    pass
                elif point == 0:
                    to_SID.append(self.to_sid)
                    from_redis_instance2.append(self.from_redis_instance)
                    source_vars["to_sid"] = to_SID
                    source_vars["from_redis_instance"] = from_redis_instance2
                    self.hosts_dicts[self.to_ip] = source_vars


            ##################################
                group_hosts_dict.append(self.from_ip)
                group_hosts_dict.append(self.to_ip)

                all_sid.append(self.from_sid)
                all_sid.append(self.to_sid)
                from_all_sid.append(self.from_sid)
                to_all_sid.append(self.to_sid)
            for i in all_sid:
                if not i in self.all_sid:
                    self.all_sid.append(i)
            for i in to_all_sid:
                if not i in self.to_all_sid:
                    self.to_all_sid.append(i)
            vars_dict["all_sid"] = all_sid
            vars_dict["from_all_sid"] = from_all_sid
            vars_dict["to_all_sid"] = to_all_sid
            self.group_vars_dict = vars_dict
            for i in group_hosts_dict:
                if not i in self.group_hosts_dict:
                    self.group_hosts_dict.append(i)

            self.add_host_var(self.hosts_dicts)
            self.add_group_var(self.group_hosts_dict, self.group_vars_dict)
                    

            return self.inventory
        except StandardError as e:
            print 'StandardError:', e
        finally:
            cursor.close()
            conn.close()

###

    def example_inventory(self):
        return { '_meta': { 'hostvars': {} } }

    # Empty inventory for testing.
    def empty_inventory(self):
        return { '_meta': { 'hostvars': {} } }

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()


    def add_host_var(self, hosts_dicts=None):
        meta_dict = self.inventory.get( "_meta", {} )
        hosts_dict = meta_dict.get( "hostvars", {} )
        #host_vars = hosts_dict.get( self.from_ip, {} )

        #host_vars["from_sid"] = self.from_sid
        #host_vars["from_redis_instance"] = self.from_redis_instance
        #host_vars["to_sid"] = self.to_sid
        #host_vars["to_ip"] = self.to_ip

        #hosts_dict = hosts_dicts
        meta_dict["hostvars"] = hosts_dicts
        self.inventory["_meta"] = meta_dict




    def add_group_var(self, group_host_dict, group_var_dict):
        group_dict = self.inventory.get( "group", {} )
        group_hosts_dict = group_dict.get( 'hosts', [] )
        group_vars_dict = group_dict.get( 'vars', {} )

        #group_vars_dict["from_sid_list"] = var_value
        #group_vars_dict["all_sid_list"] =
        #group_vars_dict["to_sid"] =

        group_dict['vars'] = group_var_dict
        group_dict['hosts'] = group_host_dict
        self.inventory["group"] = group_dict



if __name__ == "__main__":
    Inventory()
