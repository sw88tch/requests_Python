import requests

addres = 'https://docs.python.org/3.5/'
res = requests.get(addres)
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
print(res.text)
