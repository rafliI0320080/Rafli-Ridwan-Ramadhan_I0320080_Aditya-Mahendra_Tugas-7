# membuat judul program
print("===========================================")
print("======== Program Text Modification ========")
print("===========================================")
import os


def menu():
    print("Program ini dapat memodifikasi text anda sesuai kehendak anda")
    print("Menu")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Capitalize each word")
    print("4. Capitalize first word")
    print("5. Replace substring")


def uppercase():
    text = str(input("Masukkan text anda : "))
    text = text.upper()
    print("Hasil text setelah diubah adalah '%s'" % text)


def lowercase():
    text = str(input("Masukkan text anda : "))
    text = text.lower()
    print("Hasil text setelah diubah adalah '%s'" % text)


def capitalize_each_word():
    text = str(input("Masukkan text anda : "))
    text = text.title()
    print("Hasil text setelah diubah adalah '%s'" % text)


def capitalise_first_word():
    text = str(input("Masukkan text anda : "))
    text = text.capitalize()
    print("Hasil text setelah diubah adalah '%s'" % text)


def replace_substring():
    text = str(input("Masukkan text anda : "))
    n = int(input("Berapa kali anda akan mengubah substring : "))
    for i in range(n):
        ubah = str(input("Substring apa yang ingin diubah pada text : "))
        ubahtext = str(input("Substring baru : "))
        text = text.replace(ubah, ubahtext)
    print("Hasil text yang baru adalah '%s'" % text)


# sistem program
menu()
jawaban = int(input("Masukkan kode program yang ingin digunakan : "))

if (jawaban == 1):
    os.system("cls")
    uppercase()
elif (jawaban == 2):
    os.system("cls")
    lowercase()
elif (jawaban == 3):
    os.system("cls")
    capitalize_each_word()
elif (jawaban == 4): 
    os.system("cls")
    capitalise_first_word()
elif (jawaban == 5):
    os.system("cls")
    replace_substring()
else:
    print("Error!")

print("==================== Program Selesai ====================")
