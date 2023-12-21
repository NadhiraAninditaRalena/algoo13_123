class Proyek:
    def __init__(self, nama, status, estimasi_waktu):
        self.nama, self.status, self.estimasi_waktu = nama, status, estimasi_waktu

    def __repr__(self):
        return f"Proyek('{self.nama}', '{self.status}', {self.estimasi_waktu})"

proyek_list = [
    Proyek("Proyek A", "Dalam Pengerjaan", 14),
    Proyek("Proyek B", "Selesai", 10),
    Proyek("Proyek C", "Dalam Pengerjaan", 21),
    Proyek("Proyek D", "Dalam Pengerjaan", 7),
]

# masih dalam pengerjaan
proyek_dalam_pengerjaan_list = [proyek for proyek in proyek_list if proyek.status.lower() == 'dalam pengerjaan']
print("\nDaftar Proyek masih dalam pengerjaan:")
print("\n".join([f"Nama: {proyek.nama}, Status: {proyek.status}, Estimasi Waktu: {proyek.estimasi_waktu} hari" for proyek in proyek_dalam_pengerjaan_list]))

# proyek dalam pengerjaan, berdasarkan estimasi waktu penyelesaian
proyek_dalam_pengerjaan_list.sort(key=lambda x: x.estimasi_waktu)
print("\nProyek diurutkan berdasarkan estimasi waktu penyelesaian:")
print("\n".join([f"Nama: {proyek.nama}, Status: {proyek.status}, Estimasi Waktu: {proyek.estimasi_waktu} hari" for proyek in proyek_dalam_pengerjaan_list]))

