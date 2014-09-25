###Setting up the project on Amazon Linux

$ yum install git

$ git clone git://github.com/priidukull/yes_this_can_be

$ cd yes_this_can_be

$ git checkout

$ yum install postgresql93 postgresql93-server postgresql93-devel postgresql93-contrib postgresql93-docs

$ service postgresql93 initdb

$ wget https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tar.xz

$ tar xf Python-3.4.1.tar.xz 

$ cd Python-3.4.1

$ yum install gcc

$ ./configure --prefix /opt/python/3.4.1

$ make

$ make install

$ export PATH=/opt/python/3.4.1/bin:$PATH

###Running scripts to fill the database

$ vim ~/.bashrc 

export PYTHONPATH="/home/ec2-user/yes_this_can_be/"

$ python3 collectors/fill_statutes.py 

$ python3 collectors/fill_statute_xml.py 

$ python3 deriving/derive_paragraphs.py --dep

###Project Structure:

Deriving - using data inside the DB to derive new data.