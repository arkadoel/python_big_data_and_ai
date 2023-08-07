from datetime import datetime, timedelta

fecha1 = datetime(2023,1,1)
fecha2 = datetime(2023,2,1)

delta = fecha2 - fecha1
print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("segundos totales a dias", delta.total_seconds()/60/60/24)

print("\r\n#####\r\n")

fecha1 = datetime(2023,1,1) + timedelta(weeks=1) #le añadimos una semana
delta = fecha2 - fecha1
print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("segundos totales a dias", delta.total_seconds()/60/60/24)