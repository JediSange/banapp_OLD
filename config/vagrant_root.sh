#!/usr/bin/env bash
apt-get update
apt-get install -y vim
apt-get install -y git
apt-get install -y python
apt-get install -y python-virtualenv
apt-get install -y mongodb
apt-get install -y nodejs
apt-get install -y nodejs-legacy
apt-get install -y npm
npm install -g grunt-cli
npm install -g grunt-init
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
