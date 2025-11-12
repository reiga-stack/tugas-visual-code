nilai = int(input('masukan nilai:'))
usia = int(input('masukan usia:'))

if nilai>=75:
    if(usia<15):
        print('selamat adek, kamu lulus!')
    else:
        print('selamat kakak, kamu lulus!')
else:
    if(usia<15):
        print('mohon maaf adek, coba lagi ya1')
    else:
        print('mohon maaf kakak, coba lagi yaa!')