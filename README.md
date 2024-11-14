# Online shop
This implements shop

## Interaction
To use this service, access test data at onlineshop.onrender.com/kiokogit/

To run on local development mode:
Clone repository
```bash
git clone https://github.com/kiokogit/OnlineShopAPI.git
```
Create virtual env
```bash
python -m venv venv
```
install requirements using pip (or any other tool)
```bash
pip install -r requirements.txt
```
Create a .env file with the following mandatory envs
For test values... well; hold on
```bash
GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''

AFR_TKG_USERNAME = ''
AFR_TKG_API_KEY = ''
```
Create superuser
```bash
python manage.py createsuperuser
```

Run 
```bash
python manage.py runserver
```
Access the server at localhost:800 by default


## API ENDPOINTS

### login
GET
```/api/google-login```

GET 
```/api/google-callback?code=''&error=''```

### Update customer details
 - To update phone number, and other details not in oauth
 - Phone number must be valid (has country code)
 - Cannot place order without phone number

POST
```/api/update-profile```
body example: 
```json
{
    "phone_number": "+2547xxxxxx"
}
```

### Update products catalogue
- For admin, to create new products
- Item code must be unique

POST
```/api/update-items```

body example: 
```json
{
    "item_name": "Zoom Camera",
    "item_code": "ZM-002",
    "amount": 200
}
```

### Place order for item
- For customer as the logged in user

POST
```/api/place-order```

body_example: 
```json
{
    "item_code": "ZM-002"
}
```


....END...