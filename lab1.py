import requests

# step 4 of virtualenv
print(requests.__version__)

# step 5 of curl
response = requests.get('http://google.com/')
print(response)

response2 = requests.get('https://raw.githubusercontent.com/vhnguyen0707/cmput404_lab/main/lab1.py')
print(response2.text)