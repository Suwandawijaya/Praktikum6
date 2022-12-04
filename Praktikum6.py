# import tabulate
from tabulate import tabulate

# Suwana wijaya
# TI22B1

dataMahasiswa = {
    'No': [],
    'Nim': [],
    'Nama': [],
    'Tugas': [],
    'Uts': [],
    'Uas': [],
    'Nilai Akhir': []
}
no = 0
# fungsi untuk menampilkan data


def tampilkan():
    print("Berikut data yang ada")
    print(tabulate(dataMahasiswa, headers=[
        'No', 'Nim', 'Nama', 'Tugas', 'Uts', 'Uas', 'Nilai Akhir'], tablefmt="fancy_grid"))
    
#fungsi untuk menambahkan data


def tambah(no):
    # menginput data
    nim = int(input("Masukan NIM : "))
    nama = input("Masukan Nama : ")
    tugas = int(input("Masukan Nilai Tugas : "))
    uts = int(input("Masukan Nilai Uts : "))
    uas = int(input("Masukan Nilai Uas: "))
    nilai_akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 /100)
    # menambahkan data
    dataMahasiswa['No'].append(no)
    dataMahasiswa['Nim'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Uts'].append(uts)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['Uas'].append(uas)
    dataMahasiswa['Nilai Akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan.')
    # print(tabulate(dataMahasiswa, headers=[
    #     'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))

# fungsi untuk mengedit data


def ubah(nama):
    # cek jika ada nama  tersebut di dataMahasiswa
    if nama in dataMahasiswa['Nama']:
        # cari posisi indexnya lalu disimpan di nimIndex
        namaIndex = dataMahasiswa['Nama'].index(nama)
        print("Pilih Data yang mau diedit")
        # perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) Nim, \n (2) Nama, \n (3) Nilai Tugas, \n (4) Nilai Uts, \n (5) Nilai Uas, \n (0) Save Perubahan & exit \n :"))
            print("")

            if editApa == 1:
                # merubah nim
                newNim = int(input("Masukan Nim :"))
                dataMahasiswa['Nim'][namaIndex] = newNim
            elif editApa == 2:
                # merubah nama 
                newNama = input("Masukan Nama :")
                dataMahasiswa['Nama'][namaIndex] = newNama
            elif editApa == 3:
                # merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    dataMahasiswa['Uas'][namaIndex] * 35 / 100)
                dataMahasiswa['Tugas'][namaIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 4:
                # merubah nilai uts & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                nilai_akhir = (dataMahasiswa['Tugas'][namaIndex] * 30 / 100) + (newUts * 35 / 100) + (
                    dataMahasiswa['Uas'][namaIndex] * 35 / 100)
                dataMahasiswa['Uts'][namaIndex] = newUts
                dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 5:
                # mengubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                nilai_akhir = (dataMahasiswa['Tugas'][namaIndex] * 30 / 100) + (dataMahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                dataMahasiswa['Uas'][namaIndex] = newUas
                dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 0:
                print('Perubahan Data berhasil disimpan,')
                break
    else:
        print("data tidak ditemukan")

# fungsi untuk Menghapus data


def hapus(nama):
    if nama in dataMahasiswa['Nama']:
        namaIndex = dataMahasiswa['Nama'].index(nama)
        # menghapus data berdasarkan position index pada nama
        del dataMahasiswa['No'][namaIndex]
        del dataMahasiswa['Nim'][namaIndex]
        del dataMahasiswa['Nama'][namaIndex]
        del dataMahasiswa['Tugas'][namaIndex]
        del dataMahasiswa['Uts'][namaIndex]
        del dataMahasiswa['Uas'][namaIndex]
        del dataMahasiswa['Nilai Akhir'][namaIndex]
        print("data berhasil dihapus. ")
    else:
        print("data tidak ditemukan")
        
# fungsi untuk mencari data


# Melakukan perulangan menggunakan white sampai user menekan huruf Q  perulangan akan berhenti
while True:
    # opsi input pilihan C,R,U,D,F,Q
    tanya = input(
        "(C) Menambah data,\n (R) Melihat semua Data,\n (U) Update data,\n (D) Menghapus data,\n (Q) Keluar program : ")
    if tanya == "C":
        while True:
            no += 1
            # memanggil fungsi tambahan dan memparsing data no
            tambah(no)
            tambahDataLagi = input("Tambah data lagi ? (y/n) :")
            if tambahDataLagi == 'n':
                break
    elif tanya == "R":
        # menampilkan data dalam bentuk table menggunakan package tabulate
        tampilkan()
        print("")
    elif tanya == "U":
        print(tabulate(dataMahasiswa, headers=[
            'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
        nama = input('Masukan nama yang mau diedit :')
        print("")
        ubah(nama)
    elif tanya == "D":
        print(tabulate(dataMahasiswa, headers=[
            'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
        nama = input('Masukan Nama yang mau dihapus :')
        print("")
        hapus(nama)
    elif tanya == "Q":
        print("")
        print("Anda telah keluar dari program.")
        break