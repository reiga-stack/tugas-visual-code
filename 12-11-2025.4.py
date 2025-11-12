buah_yang_tersedia = {'jeruk','mangga','melon'}
buah_yang_dicari = input('masukkan nama buah dalam huruf kecil:')
if (buah_yang_dicari in buah_yang_tersedia):
    print('buah yang anda cari tersedia!')
else:
    print('buah yang cari tidak tersedia!')