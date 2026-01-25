import math

print("tekan a untuk keliling lingkaran, tekan b untuk keliling persegi")
pilihan=input("masukkan pilihan anda (a/b):")

if pilihan=="a":
    print ("keliling lingkaran")
    r=float(input("masukkan jari-jari lingkaran:"))
    keliling_lingkaran=2*math.pi*r
    print("keliling lingkaran adalah:",keliling_lingkaran)

elif pilihan=="b":
    print ("keliling persegi")
    s=float(input("masukkan sisi persegi:"))
    keliling_persegi=4*s
    print("keliling persegi adalah:",keliling_persegi)

else: 
    print("masukkan pilihan yang benar")