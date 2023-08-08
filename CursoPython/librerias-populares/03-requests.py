# temas relacionados con api rest

import requests

url = "https://jsonplaceholder.typicode.com/users"

# podremos usar .get,.put,.post,.delete,....
r = requests.get(url, timeout=10)
print(
    r.status_code,
    r.text    
    )

print("\nUsuarios del json:")
for user in r.json():
    print(user["name"])

#listar un usuario
url = "https://jsonplaceholder.typicode.com/users/1"

r = requests.get(url, timeout=10)
print(r.json())

#crear un usuario
url = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "federico fernandez"
}
r = requests.post(url, timeout=10, data=user)
print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "federico perez"
}
r = requests.put(url, timeout=10, data=user)
print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
r = requests.delete(url, timeout=10)
print(r.status_code)

"""
convencion

200 listar
201 crear
204 actualizar o eliminar

"""


