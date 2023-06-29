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


### Accounts App
Contain User model inherited from AbstractUser

Also contains two forms: CustomUserCreationForm(UserCreationForm) and CustomUserChange(UserChangeForm)

##### Contains following lines
```
first_name      CharField
last_name       CharField
phone_number    PhoneNumber
email           Email
password        Password
```

### Taxi app
This app allows to make orders to the users of Booking-API app
```
user            ForeignKey
user_name       Charfield
user_phone_number   Phone number
user_email      Email
is_econom       Boolean
is_business     Boolean
is_premium      Boolean
```
