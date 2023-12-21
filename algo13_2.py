def mata_uang(jumlah_local, kurs):
    jumlah_asing = jumlah_local / kurs
    return jumlah_asing

# Input (Rupiah)
jumlah_rupiah = float(input("Masukkan jumlah uang dalam Rupiah: "))

# Input (Dolar) ke (Rupiah)
kurs_usd_to_idr = float(input("Masukkan kurs USD terhadap Rupiah: "))

jumlah_usd = mata_uang(jumlah_rupiah, kurs_usd_to_idr)

# hasil dengan tanda mata uang
print(f"\nJumlah uang dalam USD: ${jumlah_usd:.2f}")

