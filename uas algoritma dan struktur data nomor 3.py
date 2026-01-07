def hitung_gaji(tarif, jam, hari):
    total = 0
    for _ in range(hari):
        total += 8*tarif + max(0, jam-8)*tarif*1.5 if jam > 8 else jam*tarif
    return total

print("Total gaji:",
      hitung_gaji(float(input("Tarif: ")),
                  int(input("Jam/hari: ")),
                  int(input("Hari kerja: "))))