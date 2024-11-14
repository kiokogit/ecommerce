# Online shop
This implements an imitation of an online shop with customers and items; accessed through openidconnect authed users, and social logins (Oauth2)


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

```bash
# if using google. can use any other social app for auth
GOOGLE_CLIENT_ID=clientid
GOOGLE_CLIENT_SECRET=None
SECRET_KEY=secret_key
DEBUG=True/False

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

## SWAGGER DOCUMENTATION
All the api endpoints are documented using swagger. Check it on ```{your_endpoint}/documentation/```
To get the deployed swagger docs, check out: 
![API Swagger Documentation](https://onlineshopapi-ctyo.onrender.com/documentation/)


## TESTS
To run tests using coverage
```bash
 pip install coverage
 coverage run -m pytest
 coverage report -m
```
Include OAuth2 authentication headers

## Logging In
With the app running on localhost, register an application to get an access code to interact with the app
- Go to:
```localhost:8000/o/applications```
Login to as a super user and proceed to applications
![Register app](/Screenshot%202024-11-13%20at%2023.54.49.png)

Enter credentials,
![Register app](/Screenshot%202024-11-13%20at%2023.55.27.png)

Get access code for authentication

```http://localhost:8000/o/token/``` Use BASIC AUTH for authorization

![Get code](/Screenshot%202024-11-14%20at%2009.45.54.png)

And for request body, enter the following in form data
![Get code data](/Screenshot%202024-11-14%20at%2009.49.49.png)

Success response: 

```json
{
    "access_token": "<access_token>",
    "token_type": "Bearer",
    "expires_in": 36000,
    "refresh_token": "<refresh_token>",
    "scope": "read write groups"
}
```

To call resources, add basic token authentication
![Access resources](/Screenshot%202024-11-14%20at%2009.52.52.png)

### Message service
For use of Messaging the customer
Login to Africas talking sandbox site, and get the credentials for the sandbox; When you place an order, a message should appear as below:
![AFRICA'S TALKING SCREEN](/Screenshot%202024-11-14%20at%2021.32.33.png)

## API ENDPOINTS

### Update customer details
Cannot place order without phone number

```/api/customers/```
create example: 
```json
{
    "name": "Cutomer1",
    "code": "bs001",
    "phone_number": "+2547xxxxxx" // must have country code
}
```

### Place order for item
- For customer as the logged in user

POST
```/api/orders/```

body_example: 
```json
{
    "item_name": "Sugae2",
    "amount":100.56,
    "customer_id": 1
}
```


## TEST APP
Since this is a test app, dbsqlite3 is the configured database; 
for postgres, uncomment these lines in settings.py
```py
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DATABASES_DEFAULT_ENGINE', 'django.db.backends.postgresql_psycopg2'),
#         'NAME': os.getenv('DATABASES_DEFAULT_NAME'),
#         'USER': os.getenv('DATABASES_DEFAULT_USER'),
#         'PASSWORD': os.getenv('DATABASES_DEFAULT_PASSWORD'),
#         'HOST': os.getenv('DATABASES_DEFAULT_HOST'),
#         'PORT': os.getenv('DATABASES_DEFAULT_PORT'),
#     }
# }
```
Then set the corresponding env values

## DEPLOYMENT AND CICD
This app has dev.yaml file that triggers github actions to ```deploy``` on render.com using ```DEPLOYMENT HOOK```

To set it up, 
Login to render.com and set up a new web service, and set ```autodeploy=False``` so that it does not deploy by commits, but by pull requests and push to main branch

on your github repository (if using github actions), set Repository secrets on Repository settings
add: ```RENDER_DEPLOY_HOOK_URL``` and add value from render.com service


....END...