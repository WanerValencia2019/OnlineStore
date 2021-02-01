# OnlineStore  :strawberry:
ChoquiFood is a web application, ecommerce type, where you can find a wide variety of products at your disposal, and also with very affordable prices.

Developed with Django Python framework 
:earth_asia: python-django:books:

## Installation
  - #### Download
    - ``git clone https://github.com/WanerValencia2019/OnlineStore/ nameProject``
  - #### Create a virtual environment
    - ``pip3 install venv``
    - ``python3 -m venv env``
      - ``source env/bin/activate``

  - #### Install requirements or dependencies
    - ``pip install -r requirements.txt``
    - ``cd nameProject``
  - #### Build migrations
    - Example: 
      - `` python manage.py  makemigrations appName``
      - `` python manage.py  migrate appName``
    - ***Build migrations in the following order(appName)***
      - users
      - products
      - category
      - promo_codes
      - carts
      - shipping_adress
      - billing_profiles
      - orders
      - billing_charges
      - ***finally excute***
        - `` python manage.py migrate ``
   - #### Create super user
      - ``python manage.py createsuperuser``   
   - #### Run server
     - ``python manage.py runserver 127.0.0.1:8000``
## Configuration
  - #### Create a file with name ``.env``
    - This file must contain, the following properties: ***Example***
      - SECRET_KEY= &e_#wg+qa_7tx_9m)09rs$%6&kw38umd&q0xni9*5lb*rbg62l
      - EMAIL_HOST_USER = correo@gmail.com
      - EMAIL_HOST_PASSWORD = contraseña
      - STRIPE_PUBLIC_KEY= key public for stripe
      - STRIPE_PRIVATE_KEY=key private for stripe
