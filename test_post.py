import requests
import json

url = 'http://localhost:5001/request_POSTGET'
myobj = {
            'name':'Kanisorn',
            'age':'22'
        }

x = requests.post(url, data = json.dumps(myobj))
output = json.loads(x.text)
print(output['y'])