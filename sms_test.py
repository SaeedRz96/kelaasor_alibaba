import requests
import json


api_key = ''
data = {
    'receptor' : '09129740477',
    'message' : '123456'
}
data = json.dumps(data)
response = requests.post(
    url = 'https://api.kavenegar.com/v1/{}/sms/send.json'.format(api_key),
    data=data,
    headers={'Content-Type': 'application/json'},
)

print(response)
print(response.text)
print(response.json())