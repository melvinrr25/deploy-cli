import subprocess
import json
import sys
import os

args = sys.argv
args.append(args.pop(0))
args.pop()
pemPath = args.pop()
instance_tag = args.pop()

def deploy(ip):
  print('Deploying to: {}'.format(ip))
  script_path = '{}{}'.format(os.getcwd(), '/scripts/ssh.sh')
  command = '{} {} {}'.format(script_path, pemPath, ip)
  output = subprocess.check_output(command, shell=True)
  print(output)

def fetchIpAddresses(args):
  json_string = ''.join(args)
  json_obj = json.loads(json_string)
  instances_array = list(map(lambda x: flatten(x[0]), json_obj))
  all_by_tag_mame_and_running = list(
    filter(lambda x: instance_tag in x and 'running' in x, instances_array)
  )
  ip_addresses = list(map(lambda x: x[1], all_by_tag_mame_and_running))
  for ip in ip_addresses:
    deploy(ip)

def flatten(nested_list):
  return eval('['+str(nested_list).replace('[','').replace(']','')+']')

fetchIpAddresses(args)