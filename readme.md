django-admin startproject project_name
python manage.py runserver => to start the development server

!!make migrations 
   python manage.py makemigrations
     python manage.py migrate
     

"" starting an app
      django-admin startapp app_name 

"" configure test routes in urls.py
     make the view function in views.py
       update the root urls.py to include the apps urls.py
         modify settings to include the app in the installed apps list 
          
"" creating database 
     default sqlite
       models.py and defint the schema as a class
        manipulate the db crud pos in the views.py 
          make migrations (2 commands)
          
           
# running on localhost 
   python manage.py runserver 8080       
       