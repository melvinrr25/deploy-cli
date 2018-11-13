import subprocess 
import os
import io
import time
import sys

class Deployment(object):
  def __init__(self, args):
    self.instances_tag = args['instances_tag']
    self.profile = args['profile']
    self.key_path = args['key_path']
    self.region = args['region']

  def deploy(self):
    script_path = '{}{}'.format(os.getcwd(), '/scripts/fetch_instances.sh')
    command = '{} {} {} {} {}'.format(
      script_path, 
      self.instances_tag, 
      self.key_path, 
      self.region, 
      self.profile
    )

    process = subprocess.Popen(['bash', '-c', command], stdout=subprocess.PIPE)

    while process.stdout.readable():
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode('utf-8').strip())

