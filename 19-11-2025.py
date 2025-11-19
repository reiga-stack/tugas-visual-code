# Program kategori nilai mahasiswa

# 1. Menerima input list nilai mahasiswa
nilai_input = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")

# 2. Ubah input menjadi list integer
nilai_list = [int(n.strip()) for n in nilai_input.split(",")]

# 3. Menentukan kategori setiap nilai
for nilai in nilai_list:
    if nilai >= 85:
        kategori = "A"
    elif 70 <= nilai <= 84:
        kategori = "B"
    elif 55 <= nilai <= 69:
        kategori = "C"
    else:
        kategori = "D"
    
    print(f"Nilai: {nilai} → {kategori}")
