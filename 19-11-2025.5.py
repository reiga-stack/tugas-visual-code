# Program menu daftar nama

daftar_nama = []   # list penyimpanan nama

while True:
    print("\n===== MENU =====")
    print("1. Tambah nama")
    print("2. Hapus nama")
    print("3. Tampilkan semua nama")
    print("4. Keluar")

    menu = input("Pilih menu (1-4): ")

    # 1. Tambah nama
    if menu == "1":
        nama = input("Masukkan nama yang ingin ditambahkan: ")
        daftar_nama.append(nama)
        print(f"Nama '{nama}' berhasil ditambahkan.")

    # 2. Hapus nama
    elif menu == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in daftar_nama:
            daftar_nama.remove(nama)
            print(f"Nama '{nama}' berhasil dihapus.")
        else:
            print(f"Nama '{nama}' tidak ditemukan.")

    # 3. Tampilkan semua nama
    elif menu == "3":
        print("\n--- Daftar Nama ---")
        if len(daftar_nama) == 0:
            print("Belum ada nama yang tersimpan.")
        else:
            for i, nama in enumerate(daftar_nama, start=1):
                print(f"{i}. {nama}")

    # 4. Keluar
    elif menu == "4":
        print("Program selesai. Terima kasih!")
        break

    # Jika input tidak valid
    else:
        print("Menu tidak valid! Silakan pilih 1-4.")
