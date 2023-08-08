# variables de entorno

#si tuviesemos algo como esto no podriamos subirlo a github por seguridad
#SENDGRID_API_KEY = "alsdkjalksdjlasdjflkajdsf"
#miralo en readme.md

import os

apikey = os.environ.get("SENDGRID_API_KEY")
print(apikey)