angka_list = [] # Variable angka_list masih kosong

for i in range(3): # Loop 3x
    x = int(input("Masukkan angka : ")) # Input data akan masuk ke variable x sebanyak 3 kali
    angka_list.append(x)                # Memasukkan data yang di input dari variable x ke variable angka_list

angka_terbesar = max(angka_list)        # Menggunakan function max untuk memilih nilai angka yang paling terbesar

print('Angka terbesar adalah',angka_terbesar) # Menampilkan angka yang paling terbesar