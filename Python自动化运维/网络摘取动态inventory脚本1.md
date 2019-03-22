#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json



class ExampleInventory(object):
    
    def __init__(self):
        self.inventory = {}
        self.read_cli_args() 
    
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [ hostname ]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()
 
        print json.dumps(self.inventory);

    # Example inventory for testing.
    def example_inventory(self):
        return {
            'group': {
                'hosts': ['10.0.5.17', '10.0.6.71'],
                'vars': {
                    'list': 'root',
                    'listall': ['8050', '8110', '8040']
                 }
            },
            '_meta': {
                'hostvars': {
                    '10.0.5.17':{
                        'migrate_zone_id': '115',
                        'migrate_zone_redis_port': '13789',
                        'migrate_zone_rmi_port': '11043',
                        'migrate_zone_inner_ip': '192.168.1.1',
                        'migrate_zone_pub_ip': '192.168.2.1',
                        'migrate_zone_slave_ip': '192.168.3.1',
                        'migrate_zone_master_ip': '192.168.4.1'
                    },
                    '10.0.6.71':{
                        'migrate_zone_id': '8050',
                        'migrate_zone_redis_port': '13235',
                        'migrate_zone_rmi_port': '11443',
                        'migrate_zone_inner_ip': '192.168.1.2',
                        'migrate_zone_pub_ip': '192.168.2.2',
                        'migrate_zone_slave_ip': '192.168.3.2',
                        'migrate_zone_master_ip': '192.168.4.2'
                    }
                }
            }
}


    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
