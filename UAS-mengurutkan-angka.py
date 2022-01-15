# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:50:11 2022

@author: Arini Elsa Azkaminnati
"""

angka = [] # Variable angka masih kosong

for i in range(3): # Loop 3x
    x = int(input("Masukkan angka : ")) # Input data akan masuk ke variable x sebanyak 3 kali
    angka.append(x)                     # Memasukkan data yang di input dari variable x ke variable angka
    
print ("Angka input :",angka) # Menampilkan data input di variable angka

angka.sort()                  # Mengurutkan data variable angka dari yang terkecil
print("Angka diurutkan dari yang terkecil :", angka) # Menampilkan variable angka setelah diurutkan