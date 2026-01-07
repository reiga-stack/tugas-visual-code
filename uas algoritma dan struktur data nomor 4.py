def tambah(a,b): return a+b
def kurang(a,b): return a-b
def kali(a,b): return a*b
def bagi(a,b): return "Error" if b==0 else a/b

print("1:+  2:-  3:*  4:/")
p = input("Pilih: ")
a = float(input("A: "))
b = float(input("B: "))

if p=="1": print(tambah(a,b))
elif p=="2": print(kurang(a,b))
elif p=="3": print(kali(a,b))
elif p=="4": print(bagi(a,b))
else: print("Salah pilih")
