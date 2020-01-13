import requests

ip = "http://10.10.112.87:3000/"
link = ''
result = ''
while link != 'end':
    response = requests.get(ip + link)
    json = response.json()
    print(json)
    link = json['next']
    result += json['value']
print(result[:-3])