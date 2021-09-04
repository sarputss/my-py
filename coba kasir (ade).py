import sys
total = []

print("--------------------------")
print("KASIR AA")
print("-------------------------------")

def daftar_barang():
    sedia = '''KAMI MENYEDIAKAN:
    1 Buku Tulis Campus 50 Lembar
    2 Buku Tulis Anak 50 Lembar
    3 Oil Ballpoint
    4 Pensil 2B
    5 Penghapus'''
    print(sedia)
    print('\n')
    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 7000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 3000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 4000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 6000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 5000 * jumlah5   
        total.append(total5)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        if (bayar < totalakhir):
            kurangnya = print ("Uang Anda Kurang   : ", totalakhir - bayar)
            kurangnya = totalakhir - bayar
            bayar_lagi = int(input("Bayar Lagi :"))
            kembalian = bayar_lagi - kurangnya
        elif bayar == totalakhir:
            print('Uang Anda Pas')
        else :
            kembalian = bayar - totalakhir
            print("Kembalian        :", kembalian)

        print("-------------------------------")
        print("          THANK YOU         ")
        print("-------------------------------")

daftar_barang()