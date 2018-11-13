from scripts.deployment import Deployment

deployment = Deployment({
  'key_path': '/home/melvin/Desktop/danestreet-stuff/doc-preview/test.pem',
  'region': 'us-east-1',
  'profile': 'ds-staging',
  'instances_tag': 'docpreviewapi'
})

deployment.deploy()