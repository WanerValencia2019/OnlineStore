# OnlineStore  :strawberry:
ChoquiFood es una aplicación web, tipo ecommerce, donde podrás encontrar una ampliedad variedad de productos a la disposición, y además con precios muy adsequibles.

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
