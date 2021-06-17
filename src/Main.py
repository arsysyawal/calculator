# Ini judul
print("\n\t====================> CALCULATOR  <========================\n")
print("\n\t====================> ARSY SYAWAL <========================\n")

# ini tampilan Opsi Pilihan
print("\n\t\t\t(+) PERTAMBAHAN (+)")
print("\t\t\t(-) PENGURANGAN (-)")
print("\t\t\t(*) PERKALIAN   (*)")
print("\t\t\t(/) PEMBAGIAN   (/)")

# ini inputan Opsi Pilihan
opsi_pilihan = input("\n\n\tSILAHKAN KELITIKIN SYMBOL DIATAS SESUAI KEBUTUHAN ANDA :")

# buat variable/ember sebuah tempat naro data
angka_1 = 0 # artinya ember ini cuma bisa untuk ikan jenis "INTEGER"
angka_2 = 0
jumlah = 0

info_hasil = "\nHASILNYA ADALAH      : " # ini jenis nya "STRING"
info_angka_pertama = "\nMASUKAN NILAI PERTAMA MU :"
info_angka_kedua = "MASUKAN NILAI KEDUA MU :"
info_penutup = "\n\t\t~~~~~~~~~~> TERIMA KASIH <~~~~~~~~~~\n"

# validasi/pengecekan dari inputan 'opsi_pilihan'
if (opsi_pilihan == '+'): # Kondisi 1: cek jika opsi pilihan 1
    angka_1 = (int(input("\nMASUKAN NILAI PERTAMA MU : "))) # ini adalah fungsi/function/method/methode
    angka_2 = (int(input("MASUKAN NILAI KEDUA MU   : ")))
    jumlah = angka_1 + angka_2

    print(f"{info_hasil}{jumlah}")
    print(f"{info_penutup}")
elif (opsi_pilihan == '-'): # Kondisi 1: cek jika opsi pilihan 2
    angka_1 = (int(input("\nMASUKAN NILAI PERTAMA MU : ")))
    angka_2 = (int(input("MASUKAN NILAI KEDUA MU   : ")))
    jumlah = angka_1 - angka_2

    print(f"{info_hasil}{jumlah}")
    print(f"{info_penutup}")
elif (opsi_pilihan == '*'):
    angka_1 = (int(input("\nMASUKAN NILAI PERTAMA MU : ")))
    angka_2 = (int(input("MASUKAN NILAI KEDUA MU   : ")))
    jumlah = angka_1 * angka_2

    print(f"{info_hasil}{jumlah}")
    print(f"{info_penutup}")
elif (opsi_pilihan == '/'):
    angka_1 = (int(input("\nMASUKAN NILAI PERTAMA MU : ")))
    angka_2 = (int(input("MASUKAN NILAI KEDUA MU   : ")))
    jumlah = angka_1 / angka_2

    print(f"{info_hasil}{jumlah}")
    print(f"{info_penutup}")

else: print("\n\t\tMAAF, PILIHAN OPSI MU TIDAK TERDAFTAR")
