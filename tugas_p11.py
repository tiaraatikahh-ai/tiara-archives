tinggi = int(input("Masukkan tinggi segitiga: "))
character = input("Masukkan karakter: ")

for i in range(1, tinggi + 1):
    print(" " * (tinggi - i) + character * (2*i - 1))

   