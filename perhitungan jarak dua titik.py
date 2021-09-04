# Perhitungan Jarak Dua Titik

import math

print('Perhitungan Jarak Dua Titik')

x1 = int(input('X1='))
y1 = int(input('Y1='))
x2 = int(input('X2='))
y2 = int(input('Y2='))

# Perhitungan jarak
jarak = math.sqrt ((x2 - x1) * (x2 - x1) + \
					(y2 - y1) * (y2 - y1))

#Hasil
print('Jarak=', jarak)

