aws_account_attribute Look up AWS account attributes.                      
aws_service_ip_ranges Look up the IP ranges for services provided in AWS su...
aws_ssm               Get the value for a SSM parameter or all parameters u...
cartesian             returns the cartesian product of lists               
chef_databag          fetches data from a Chef Databag                     
config                Lookup current Ansible configuration values          
conjur_variable       Fetch credentials from CyberArk Conjur.              
consul_kv             Fetch metadata from a Consul key value store.        
cpm_metering          Get Power and Current data from WTI OOB/Combo and PDU...
cpm_status            Get status and parameters from WTI OOB and PDU device...
credstash             retrieve secrets from Credstash on AWS               
csvfile               read data from a TSV or CSV file                     
cyberarkpassword      get secrets from CyberArk AIM                        
dict                  returns key/value pair items from dictionaries       
dig                   query DNS using the dnspython library                
dnstxt                query a domain(s)'s DNS txt fields                   
env                   read the value of environment variables              
etcd                  get info from an etcd server                         
file                  read file contents                                   
fileglob              list files matching a pattern                        
filetree              recursively match all files in a directory tree      
first_found           return first file found from list                    
flattened             return single list completely flattened              
grafana_dashboard     list or search grafana dashboards                    
hashi_vault           retrieve secrets from HashiCorp's vault              
hiera                 get info from hiera data                             
indexed_items         rewrites lists to return 'indexed items'             
ini                   read data from a ini file                            
inventory_hostnames   list of inventory hosts matching a host pattern      
items                 list of items                                        
k8s                   Query the K8s API                                    
keyring               grab secrets from the OS keyring                     
lastpass              fetch data from lastpass                             
lines                 read lines from command                              
list                  simply returns what it is given.                     
mongodb               lookup info from MongoDB                             
nested                composes a list with nested elements of other lists  
nios                  Query Infoblox NIOS objects                          
nios_next_ip          Return the next available IP address for a network   
nios_next_network     Return the next available network range for a network...
onepassword           fetch field values from 1Password                    
onepassword_raw       fetch raw json data from 1Password                   
password              retrieve or generate a random password, stored in a f...
passwordstore         manage passwords with passwordstore.org's pass utilit...
pipe                  read output from a command                           
random_choice         return random element from list                      
redis                 fetch data from Redis                                
redis_kv              fetch data from Redis                                
sequence              generate a list based on a number sequence           
shelvefile            read keys from Python shelve file                    
subelements           traverse nested key from a list of dictionaries      
template              retrieve contents of file after templating with Jinja...
together              merges lists into synchronized list                  
url                   return contents from URL                             
vars                  Lookup templated value of variables                  
