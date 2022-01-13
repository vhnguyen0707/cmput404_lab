import requests
import os

# step 4 of virtualenv
print(requests.__version__)

# step 5 of curl
response = requests.get('http://google.com/')
print(response.json())