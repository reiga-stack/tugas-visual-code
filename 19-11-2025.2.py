# Program menghitung total belanja dengan diskon

# 1. Menerima input jumlah item
jumlah_item = int(input("Masukkan jumlah item belanja: "))

# 2. Input harga setiap item dan simpan dalam list
daftar_harga = []
for i in range(jumlah_item):
    harga = int(input(f"Masukkan harga item ke-{i+1}: "))
    daftar_harga.append(harga)

# 3. Hitung total
total_sebelum = sum(daftar_harga)

# 4. Tentukan diskon
if total_sebelum >= 300000:
    diskon = total_sebelum * 0.10   # 10%
else:
    diskon = 0

# 5. Total akhir
total_akhir = total_sebelum - diskon

# Output
print("\n--- Rincian Belanja ---")
print("Daftar harga:", daftar_harga)
print("Total sebelum diskon :", total_sebelum)
print("Diskon              :", int(diskon))
print("Total akhir         :", int(total_akhir))
