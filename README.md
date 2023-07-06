# Booking-API (Booking appointment is now easier)

## Thank to [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/). This API is created using these two Python Frameworks. DRF Spectacular allows Frontend Developers to understand the documentation of the Booking-API

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

##### Contains following lines - for Bookers (create_user)

```
first_name      CharField (max_length - 50)
last_name       CharField (max_length - 50)
phone_number    PhoneNumber (max_length - 17)
email           Email
password        Password
is_user         Boolean (default=True)
```

##### Contains following lines - for Taxi drivers (create_user_taxi)

```
first_name      CharField (max_length - 50)
last_name       CharField (max_length - 50)
phone_number    PhoneNumber
email           EmailField
password        PasswordField
is_taxi         Bool (default=True)
car_size        Charfield(choices=['small', 'medium', 'big'])
```

### Taxi app

This app allows to make orders to the users of Booking-API app

```
user            ForeignKey
user_name       Charfield
user_phone_number   Phone number
user_email      Email
location        CharField(max_length = 200)
destination        CharField(max_length = 200)
is_econom       Boolean
is_business     Boolean
is_premium      Boolean
```

This app also has a calculator which help to calculate price of order using <i>geopy</i> library.

To install <i>geopy</i> type the following command to CMD:
```
pip install geopy
```

### Models of other apps will be ready after the release of first version

### Hotel App

This app helps to book a room from hotels for the users of the Booking-API.

##### Models:
 - Hotel
 - HotelRoomOrder

###### Hotel
 - Hotel ID (automatically generates the 6-digit ID)
 - Hotel name
 - <b>Hotel Location</b> - (this field is URLField, while registring new hotel it will be required to paste the url of location of the hotel from <i>Google Maps</i>)
 - <b>Minimum Price</b> - it is required field
 - <b>Phone number</b> - this field takes the number of phone of hotel
 - <b>Optionan Fields are - Hotel email and website (both will be URL Fields)</b>
 - <b>Start of the work </b> - TimeField
 - <b>End of the working hours - TimeField</b>
 - !!! All BOTH FIELDS ABOVE REQUIRED BECAUSE BOOKERS SHOULD KNOW THE OPEN HOURS OF RECEPTION AT HOTELS.!!!
 - <b>3 image fields will be required.</b>

##### HotelRoomOrder model
 - OrderID - UUID4
 - Number of Rooms - this field is required because hotel reception should know how many rooms are booked by app user.
 - Number of people.
 - date_start
 - date_to
 - additional_points - TextField() the following field is added because some customers may need additional things from hotel for example a conference room or a fitness club from hotel. Therefore this field is added.