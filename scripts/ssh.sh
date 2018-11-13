#!/bin/bash
ssh -i $1 -oStrictHostKeyChecking=no ec2-user@$2 -y << ENDSSH
  sudo fuser -k -n tcp 3000
  sudo rm -rf ~/api
  sudo git clone https://github.com/melvinrr25/fileToPdfConversor.git ./api
  sudo chown -R ec2-user:ec2-user ~/api
  cd ~/api
  sudo chmod +x ./unoconv
  sudo cp ./unoconv /usr/bin
  cd ~/api
  npm install
  sudo echo "export PORT=3000" >> ~/.bashrc
  sudo echo "export API_KEY=bWVsdmlucm9kcmlndWV6cm9kcmlndWV6Cg==" >> ~/.bashrc
  cd ~/api
  sudo pm2 start index.js
  sudo pm2 startup
  sudo pm2 save
ENDSSH
