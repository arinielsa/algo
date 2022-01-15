angka_list = [] # Variable angka_list masih kosong

for i in range(9): # Loop 9x
    x = int(input("Masukkan angka : ")) # Input data akan masuk ke variable x sebanyak 9 kali
    angka_list.append(x)                # # Memasukkan data yang di input dari variable x ke variable angka_list

y = int(input('Cari apa nich : '))      # Input menanyakan apa yang harus dicari duplikatnya

print ('Angka' ,y, 'muncul sebanyak' ,angka_list.count(y), 'kali') # Menampilkan data duplikat yang sudah dipilih
