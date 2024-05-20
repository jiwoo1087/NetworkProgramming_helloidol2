# helloidol2
---
1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > Settings.. > Language $& Frameworks > Django
   4. Run > Edit Configurations.. > + > Django Sever > Name : runserver
   5. VCS > Enable Version Control Intergration.. > git > ok
2. startapp boynextdoor
   1.python manage.py boynextdoor
   6. 'boynextdoor', in INSTALLED_APPS
3. boynextdoor/
   1. models
      1. Character
         1. name, feature, created_at, update_at
         2. __str__():객체를 츨략할 때, 알맞은 string으로 출력하자
      2. python manage.py makemigrations boynextdoor
      3. python manage.py migrate boynextdoor
   2. admin
      1. Character
      2. python manage.py createsuperuser
   3. views
      1. R: CharacterListView 
   4. templates/boynextdoor/
      1. character_list.html
   5. urls
      1. boynextdoor:chatacter_list