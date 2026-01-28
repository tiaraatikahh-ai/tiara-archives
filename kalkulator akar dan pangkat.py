import math

print("perhitungan akar dan pangkat")
print(" tekan a untuk akar kuadrat\n tekan b untuk pangkat")
pilihan = input ("masukkan pilihan anda (a/b):")

if pilihan == "a":
    angka = float(input("masukkan angka yang ingin diakar kuadratkan:"))
    hasil = math.sqrt(angka)
    print("akar kuadrat dari", angka, "adalah", hasil)

elif pilihan == "b":
    angka = float(input("masukkan angka yang ingin anda pangkatkan:"))
    pangkat = float(input("masukkan pangkatnya:"))
    hasil = math.pow(angka, pangkat)
    print(angka, pangkat, "adalah", hasil)

else:
    print("masukkan pilihan yang benar")