#!/bin/bash

# set env variable
LANG="en_US.utf8"
LC_COLLATE="C"
LC_CTYPE="C"
LC_MESSAGES="C"
LC_MONETARY="C"
LC_NUMERIC="C"
LC_TIME="C"
LC_ALL="C"

# install pyenv
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev
sudo apt-get install -y git
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo 'export PATH="/home/ubuntu/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
echo 'source .bashrc' >> ~/.bash_profile
source .bash_profile

# install python
pyenv install 3.6.9
pyenv versions

# virtualenv
sudo apt-get install -y python-virtualenv
pyenv virtualenv 3.6.9 python3
pyenv global python3

# autoenv
git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
echo 'source ~/.autoenv/activate.sh' >> ~/.bash_profile
source .bash_profile
mkdir python3
echo 'pyenv deactivate' >> ~/.env
echo 'pyenv activate python3' >> ~/python3/.env
