#import time
#print(time.time()) #time stamp desde 1/1/1970 utc



from datetime import datetime
fecha = datetime(2023,8,7)
print(fecha)

fecha2 = datetime(2023,9,7)

ahora = datetime.now()

#el formato (lo llaman directives) viene de https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
fechastr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechastr)

print(fecha.strftime("%Y.%m.%d"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
    fecha.second,
    fecha.min,
    fecha.max

)