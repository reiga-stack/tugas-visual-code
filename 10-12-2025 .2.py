listkota=[
    'jakarta','surabaya','depok','bekasi','solo',
    'jogjakarta','semarang','pkp'
]
KotaYangDicari = input('ketik nama kota yang kamu cari:')
for i, kota in enumerate(listkota):
    #kita ubah katanya ke lowercase agar
    #menjadi case insensitive
    if kota.lower() == KotaYangDicari.lower():
        print('kota yang anda cari berada pada indeks',i)
    break
else:
    print ('maaf, kota yang anda cari tidak ada')