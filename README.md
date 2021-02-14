# avalita-backend

In order to get started, clone this repo and run the following commands
```
mkvirtualenv avalita
pip install -r requirements.txt
python manage.py migrate
```

Now run the following and you will be prompted to insert a password twice.
```
python manage.py createsuperuser --user admin --email ''
```
After running
```
python manage.py runserver
```
you will be able to:
1. acess avalita at http://127.0.0.1:8000/avalita/
2. manage the database at http://127.0.0.1:8000/admin/ (acess with login "admin" and the password you just created)

Now, feel free to create some users via django-allauth avalita's sign up page (with email @ga.ita.br for students or @gp.ita.br for professors).
The confirmation email is just a directory 'sent_emails' in the root of your version of this repo.
