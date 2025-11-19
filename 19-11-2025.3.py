# Program menghitung jumlah angka genap dan ganjil

# 1. Menerima input 5 angka dari user
angka_list = []
for i in range(5):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

# 2. Hitung jumlah genap dan ganjil menggunakan percabangan
jumlah_genap = 0
jumlah_ganjil = 0

for angka in angka_list:
    if angka % 2 == 0:   # percabangan
        jumlah_genap += 1
    else:
        jumlah_ganjil += 1

# 3. Tampilkan hasil
print("\n--- Hasil ---")
print("List angka:", angka_list)
print("Jumlah angka genap :", jumlah_genap)
print("Jumlah angka ganjil:", jumlah_ganjil)
