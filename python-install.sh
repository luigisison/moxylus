#--------------------------------------------------
# Install Dependencies
#--------------------------------------------------
echo -e "\n---- Install tool packages ----"
sudo apt-get install wget subversion git bzr bzrtools python-pip gdebi-core -y
	
echo -e "\n---- Install python packages ----"
sudo apt-get install python-dateutil python-feedparser python-ldap python-libxslt1 python-lxml \
python-mako python-openid python-psycopg2 python-pybabel python-pychart python-pydot \
python-pyparsing python-reportlab python-simplejson python-tz python-vatnumber \
python-vobject python-webdav python-werkzeug python-xlwt python-yaml python-zsi \
python-docutils python-psutil python-mock python-unittest2 python-jinja2 python-pypdf \
python-decorator python-requests python-passlib python-argparse python-gdata \
python-gevent python-greenlet python-imaging python-markupsafe python-qrcode \
python-six python-suds python-usb python-wsgiref python-xlrd python-yaml \
ttf-dejavu python-pil -y
	
echo -e "\n---- Install python libraries ----"
sudo pip install gdata psycogreen

echo -e "\n--- Install other required packages"
sudo apt-get install node-clean-css -y
sudo apt-get install node-less -y
sudo apt-get install python-gevent -y

echo -e "\n--- Create symlink for node"
sudo ln -s /usr/bin/nodejs /usr/bin/node

echo -e "\n---- Install pytz ----"
sudo chown moxylus: /usr/local/lib/python2.7/dist-packages/
chmod u_w /usr/local/lib/python2.7/dist-packages/
easy_install --upgrade pytz
