# For installation
python3 -m venv virt_env && source virt_env/bin/activate
pip install -r requirements.txt

python3 manage.py migrate
python3 manage.py createsuperuser
        initial username:admin
                email :anoopchandran191990@gmail.com
                password:admin 

python3 manage.py makemigrations todo_app
python3 manage.py migrate


python3 manage.py runserver