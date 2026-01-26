import math

print(" tekan a untuk keliling lingkaran\n tekan b untuk keliling persegi\n tekan c untuk segitiga\n tekan d untuk jajargenjang")
pilihan=input("masukkan pilihan anda (a/b/c/d):")

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

elif pilihan=="c":
    print ("keliling segitiga")
    a=float(input("masukkan alas segtiga:"))
    t=float(input("masukkan tinggi segitiga:"))
    keliling_segitiga=(a*t)/2
    print("keliling segitiga adalah :",keliling_segitiga)

elif pilihan=="d":
    print ("keliling jajargenjang")
    a=float(input("masukkan panjang horizontal:"))
    b=float(input("masukkan panjang miring:"))
    keliling_jajargenjang=(2*a)+(2*b)
    print("keliling jajargenjang adalah :",keliling_jajargenjang)

else: 
    print("masukkan pilihan yang benar")