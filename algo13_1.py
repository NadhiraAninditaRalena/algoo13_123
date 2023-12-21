# Input nilai 
nilai_siswa = [float(x) for x in input("Masukkan nilai siswa (pisahkan dengan koma): ").split(',')]

# rata-rata nilai kelas
rata_rata_kelas = sum(nilai_siswa) / len(nilai_siswa)

# nilai di atas rata-rata
siswa_diatas_rata = [f"Siswa {i+1}" for i, nilai in enumerate(nilai_siswa) if nilai > rata_rata_kelas]

# hasil
print(f"\nRata-rata kelas: {rata_rata_kelas}")
print(f"Nilai siswa: {nilai_siswa}")
print(f"Siswa yang mendapatkan nilai di atas rata-rata: {', '.join(siswa_diatas_rata)}")

