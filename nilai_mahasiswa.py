# Program Perhitungan Nilai Mahasiswa

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir
nilai_akhir = (
    (nilai_tugas * 0.30) +
    (nilai_uts * 0.30) +
    (nilai_uas * 0.40)
)

# Menentukan status kelulusan
if nilai_akhir >= 60:
    status = "Lulus"
else:
    status = "Belum Lulus"

# Menampilkan hasil
print("\n=== HASIL PERHITUNGAN NILAI ===")
print("Nama Mahasiswa :", nama)
print("Nilai Akhir    :", round(nilai_akhir, 2))
print("Status         :", status)