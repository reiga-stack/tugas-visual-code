# Program deret angka menggunakan list
deret = []

for i in range(1, 6):
    deret.append(i)
print("Deret awal:", deret)

deret.extend([6, 7, 8])
deret.insert(0, 0)
deret.remove(4)
deret.pop()
deret.sort()
deret.reverse()

print("Deret akhir:", deret)
print("Jumlah elemen:", len(deret))
