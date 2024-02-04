python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r ./testweb/requirements.txt

python3 testweb/manage.py makemigrations

python3 testweb/manage.py migrate

python3 testweb/manage.py runserver
