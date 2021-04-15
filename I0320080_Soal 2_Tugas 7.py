import math
import os

# membuat judul program
print("===========================================")
print("======== Program Matematika Is Fun ========")
print("===========================================")


def menu():
    print("Menu Program yang tersedia: ")
    print("1. Program pengecek bilangan prima")
    print("2. Program hitung luas dan keliling lingkaran")
    print("3. Program hitung luas permukaan dan volume kubus")
    print("4. Program hitung luas permukaan dan volume balok")


def prima():
    num = int(input("Masukkan angka : "))
    angka = num
    num = math.sqrt(num)
    num = math.trunc(num)
    p = 0

    for j in range(1, num + 1):
        if (angka % j) == 0:
            p += 1
        else:
            continue

    if (angka == 1):
        print("%d bukan bilangan prima" % angka)
    elif (p == 1):
        print("%d adalah bilangan prima" % angka)
    elif (angka == 0):
        print("%d merupakan bilangan nol" % angka)
    else:
        print("%d bukan bilangan prima" % angka)


def lingkaran():
    menu = int(input("Diketahui (1)jari-jari atau (2)diameter tuliskan angkanya"))
    if (menu == 1):
        r = float(input("Masukkan jari-jari : "))
        luas = math.pi * (math.pow(r, 2))
        keliling = math.pi * 2 * r
        print("Luas lingkaran adalah %f Satuan" % luas)
        print("Keliling lingkaran adalah %f Satuan" % keliling)
    elif (menu == 2):
        d = float(input("Masukkan diameter : "))
        d /= 2
        luas = math.pi * (math.pow(d, 2))
        keliling = math.pi * 'r'
        print("Luas lingkaran adalah", luas, "Satuan")
        print("Keliling lingkaran adalah %f Satuan" % keliling)
    else:
        print("input salah")


def kubus():
    sisi = float(input("Masukkan panjang sisi kubus : "))
    luas_permukaan = 6 * (math.pow(sisi, 2))
    volume = math.pow(sisi, 2)
    print("Luas permukaan kubus adalah %f Satuan" % luas_permukaan)
    print("Volume kubus adalah %f satuan" % volume)


def balok():
    panjang = float(input("Masukkan panjang balok : "))
    lebar = float(input("Masukkan lebar balok : "))
    tinggi = float(input("Masukkan tinggi balok : "))
    volume = panjang * lebar * tinggi
    luas_permukaan = ((panjang * lebar * 2) + (panjang * tinggi * 2) + (lebar * tinggi * 2))
    print("Luas permukaan balok adalah %f Satuan" % luas_permukaan)
    print("Volume balok adalah %f satuan" % volume)


# sistem kerja program
jawaban = "YA"
while (jawaban == "YA"):
    os.system("cls")
    menu()
    n = int(input("\nMasukkan kode angka program yang dipilih : "))
    if (n == 1):
        os.system("cls")
        prima()
        jawaban = str(input("Apakah anda ingin menggunakan program lagi (YA/TIDAK) : "))
        jawaban = jawaban.upper()
    elif (n == 2):
        os.system("cls")
        lingkaran()
        jawaban = str(input("Apakah anda ingin menggunakan program lagi (YA/TIDAK) : "))
        jawaban = jawaban.upper()
    elif (n == 3):
        os.system("cls")
        kubus()
        jawaban = str(input("Apakah anda ingin menggunakan program lagi (YA/TIDAK) : "))
        jawaban = jawaban.upper()
    elif (n == 4):
        os.system("cls")
        balok()
        jawaban = str(input("Apakah anda ingin menggunakan program lagi (YA/TIDAK) : "))
        jawaban = jawaban.upper()
    else:
        print("Error!")
print("==================== Program Selesai ====================")