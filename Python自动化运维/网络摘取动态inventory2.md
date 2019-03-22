#!/usr/bin/env python

'''
Custom dynamic inventory script that retrieves host variables from a SQLite database
Adapted from [Creating custom dynamic inventories for Ansible | Jeff Geerling](http://www.jeffgeerling.com/blog/creating-custom-dynamic-inventories-ansible)
'''

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

import sqlite3





class Inventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()


        # Called with `--list`
        if self.args.list:
            self.populate_from_db()

        # Called with `--host [hostname]`
        elif self.args.host:
            # Not implemented, since we return `_meta` key for `--list` call
            self.inventory = self.empty_inventory()

        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()


        print json.dumps(self.inventory);



    def populate_from_db(self):
        conn = sqlite3.connect('dynamic_vars.db')


        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        curs.execute('SELECT host_name, var_name, var_value FROM host_vars;')
        vars_ = curs.fetchall()

        for v in vars_:
            self.add_host_var(v['host_name'], v['var_name'], v['var_value'])


        conn.row_factory = sqlite3.Row
        curs = conn.cursor()

        curs.execute('SELECT group_name, var_name, var_value FROM group_vars;')
        vars_ = curs.fetchall()

        for v in vars_:
            self.add_group_var(v['group_name'], v['var_name'], v['var_value'])


        return self.inventory



    # Example inventory for testing.
    def example_inventory(self):
        return { '_meta': { 'hostvars': {} } }



    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}



    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()



    def add_host_var(self, host_name, var_name, var_value):
        meta_dict = self.inventory.get( '_meta', {} )
        hosts_dict = meta_dict.get( 'hostvars', {} )
        host_vars = hosts_dict.get( host_name, {} )

        host_vars[var_name] = var_value

        hosts_dict[host_name] = host_vars
        meta_dict = hosts_dict
        self.inventory['_meta'] = meta_dict



    def add_group_var(self, group_name, var_name, var_value):
        group_dict = self.inventory.get( group_name, {} )
        group_vars_dict = group_dict.get( 'vars', {} )

        group_vars_dict[var_name] = var_value

        group_dict['vars'] = group_vars_dict
        self.inventory[group_name] = group_dict




# Get the inventory
Inventory()
