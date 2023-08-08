

import requests

url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "123456"
headers = {
    "Authorization" : f"Bearer {apikey}"
}

#añadimos el parametro headers
r = requests.post(url, timeout=10, headers=headers, data="")
print(r.status_code)

if r.status_code == 200:
    print(r.json()) #resultado en formato json