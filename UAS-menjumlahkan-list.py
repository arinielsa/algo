list1 = [1, 2, 3] # Variable list1
list2 = [4, 5, 6] # Variable list2

rekap = zip(list1, list2) # Mengumpulkan data variable list1 dan list2

hasil = [x + y for (x, y) in rekap] # Penjumlahan 1+4, 2+5, 3+6

print(hasil) # Menampilkan hasil penjumlahan