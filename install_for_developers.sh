# Filename: install_for_developers.sh
# Author:   LIU Yang
# Create Time: Thu Oct 31 13:03:20 HKT 2013
# License:     LGPL v2.0+
# Contact Me:  JeremyRobturtle@gmail.com
# Brief: Just make symlinks

# If you didn't add ~/bin to your PATH
# I suppose you didn't changed default shell either :-)
test -d ~/bin || echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
test -d ~/bin || mkdir ~/bin
test -d ~/Templates || mkdir ~/Templates

ln -s $(pwd)/newycm_extra_conf.py ~/bin
for template in $(ls ycm.*.py); do
    ln -s $(pwd)/"$template" ~/Templates
done
