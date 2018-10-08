mkdir beitech_test
cd beitech_test
mkdir beitech_store
cd beitech_store
git clone https://github.com/josdavidmo/beitech_test.git .
cd ..
virtualenv -p python3 env
source env/bin/activate
cd beitech_store
pip3 install -r requirements.txt
python3 manage.py migrate
sqlite3 db.sqlite3 < doc/data.sql
python3 manage.py runserver

sudo apt install virtualenv
