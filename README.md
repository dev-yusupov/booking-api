# Booking-API (Booking appointment is now easier)

##### Thank to [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/). This API is created using these two Python Frameworks. DRF Spectacular allows Frontend Developers to understand the documentation of the Booking-API.

<h5 style="color:rgb(30,150,150);">Booking-API help to book from the following services</h5>

- Booking Appointment in a **hospital**
- Booking tickets to **airlines**
- Booking tickets to **concerts**
- Request **a taxi**
- Food Delivery
- Booking Hotel

### How to start

1. Clone the Repository from GitHub and enter into repo from command line
   
```
git clone https://github.com/dev-yusupov/booking-api.git
cd booking-api
```

2. Install requirements

```
pip install -r requirements.txt
```

2. Make migrations

```
python manage.py makemigrations
python manage.py migrate
```

3. Run server
   
```
python manage.py runserver
```

# Features
#### Project apps

```
booking-api
|____ config
|      |___ __init__.py
|      |____asgi.py
|      |____settings.py
|      |____urls.py
|      |____wsgi.py
|_____accounts
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ forms.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|____ taxi
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|____ hotel
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|____ hospital
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|____ entertainment
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|____ airline
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|____ delivery
|      |____ __init__.py
|      |____ admin.py
|      |____ apps.py
|      |____ models.py
|      |____ serializers.py
|      |____ tests.py
|      |____ urls.py
|      |____ views.py
|
|_____ manage.py
|_____ README.md
|_____ requirements.txt
|_____ .gitignore
```


### Config
URLs of apps

```
/api/accounts/  ---  Accounts app
/api/taxi/  ---  Taxi app
/api/hotel/ --- Hotel app
/api/hospital/  --- Hospital app
/api/entertainment/ --- Entertainment app
/api/delivery/ --- Delivery app
/api/airline/ --- Airline app
```


### Accounts App
Contain User model inherited from AbstractUser

Also contains two forms: CustomUserCreationForm(UserCreationForm) and CustomUserChange(UserChangeForm)
