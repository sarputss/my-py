
print('PENENTUAN NAMA HARI')
print('------------------------------------------')

print('\n')
hari = '''
1 SENIN
2 SELASA
3 RABU
4 KAMIS
5 JUMAT
6 SABTU
7 MINGGU '''
print(hari)
print('\n')

kodeHari = int(input('MASUKKAN KODE HARI = '))

#penentuan nama hari
if kodeHari == 1:
	print('SENIN')
elif kodeHari == 2:
	print('SELASA')
elif kodeHari == 3:
	print('RABU')
elif kodeHari == 4:
	print('KAMIS')
elif kodeHari == 5:
	print('JUMAT')
elif kodeHari == 6:
	print('SABTU')
elif kodeHari == 7:
	print('MINGGU')
else:
	print('KODE SALAH :( ')
