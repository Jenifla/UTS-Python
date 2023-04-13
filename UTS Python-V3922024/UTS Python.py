#!/usr/bin/env python
# coding: utf-8

# In[1]:


#membuat koneksi ke server database
import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = ""
)

cursor = db.cursor()

#menjalankan query membuat database
cursor.execute("CREATE DATABASE db_V3922024")


# In[2]:


#menghubungkan ke server database MySQL
import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    passwd = "",
    database ="db_V3922024"
)

#mengakses dan memanipulasi data dalam database
cursorObject = db.cursor()

#menjalankan query membuat tabel mata kuliah
cursorObject.execute("""CREATE TABLE Stok_barang (
                Id_barang VARCHAR(20) PRIMARY KEY,
                Nama_barang VARCHAR(100),
                Harga_barang INT,
                Stok_awal INT,
                Barang_masuk INT,
                Barang_keluar INT,
                Stok_akhir INT
                )""")

#menutup koneksi database
db.close()


# In[ ]:


#menghubungkan ke server database MySQL
import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    passwd = "",
    database ="db_V3922024"
)

#mengakses dan memanipulasi data dalam database
cursorObject = db.cursor()

#Fungsi untuk menambahkan data
def insert_data():
    Id_barang = input("Masukkan ID Barang: ")
    Nama_barang = input("Masukkan Nama Barang: ")
    Harga_barang = int(input("Masukkan Harga Barang: "))
    Stok_awal = int(input("Masukkan Stok Awal Barang: "))
    Barang_masuk = int(input("Masukkan Jumlah Barang Masuk: "))
    Barang_keluar = int(input("Masukkan Jumlah Barang Keluar: "))
    Stok_akhir = Stok_awal + Barang_masuk - Barang_keluar
    
    #query insert data ke tabel Stok barang
    sql = "INSERT INTO Stok_barang (Id_barang, Nama_barang, Harga_barang, Stok_awal, Barang_masuk, Barang_keluar, Stok_akhir) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_barang, Nama_barang, Harga_barang, Stok_awal, Barang_masuk, Barang_keluar, Stok_akhir)
    cursorObject.execute(sql, val)
    db.commit()
    print("Stok Akhir Barang: ", Stok_akhir)
    print(cursorObject.rowcount, "Data berhasil ditambahkan")

#fungsi menampilkan data dari database
def show_data():
    cursorObject.execute("SELECT * FROM Stok_barang")
    result = cursorObject.fetchall()
    for x in result:
        print(x)

#fungsi update data database
def update_data():
    cursorObject.execute("SELECT * FROM Stok_barang")
    result = cursorObject.fetchall()
    
    print("Data sebelum diubah:")
    for x in result:
        print(x)
    
    Id_barang = input("Masukkan id barang yang ingin diubah: ")
    Nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
    Harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
    Stok_awal_baru = input("Masukkan stok awal (kosongkan jika tidak ingin mengubah): ")
    Stok_masuk_baru = input("Masukkan jumlah barang masuk (kosongkan jika tidak ingin mengubah): ")
    Stok_keluar_baru = input("Masukkan jumlah barang keluar (kosongkan jika tidak ingin mengubah): ")

    for x in result:
        if x[0] == Id_barang:
            Nama_lama = x[1]
            Harga_lama = x[2]
            Stok_awal_lama = x[3]
            Barang_masuk_lama = x[4]
            Barang_keluar_lama = x[5]
            Stok_akhir_lama = x[6]
            
            if Nama_baru:
                Nama_lama = Nama_baru
            if Harga_baru:
                Harga_lama = Harga_baru
            if Stok_awal_baru:
                Stok_awal_lama = int(Stok_awal_baru)
            if Stok_masuk_baru:
                Barang_masuk_lama = int(Stok_masuk_baru)
            if Stok_keluar_baru:
                Barang_keluar_lama = int(Stok_keluar_baru)
                
            Stok_akhir_lama = Stok_awal_lama + Barang_masuk_lama - Barang_keluar_lama

            cursorObject.execute("UPDATE Stok_barang SET Nama_barang = %s, Harga_barang = %s, Stok_awal = %s, Barang_masuk = %s, Barang_keluar = %s, Stok_akhir = %s WHERE Id_barang = %s", (Nama_lama, Harga_lama, Stok_awal_lama, Barang_masuk_lama, Barang_keluar_lama, Stok_akhir_lama, Id_barang))
            db.commit()
            
            break
            
    cursorObject.execute("SELECT * FROM Stok_barang")
    result = cursorObject.fetchall()
    print("Data setelah diubah:")
    for x in result:
        print(x)

#fungsi hapus data 
def delete_data():
    Id_barang = input("Masukkan ID Barang yang Ingin Dihapus: ")
    sql = "DELETE FROM Stok_barang WHERE Id_barang = %s"
    val = (Id_barang,)
    cursorObject.execute(sql, val)
    db.commit()
    print(cursorObject.rowcount, "Data berhasil dihapus")

#fungsi untuk mencari data berdasarkan keyword
def search_data():
    keyword = input("Masukan keyword: ")
    cursorObject.execute("SELECT * FROM Stok_barang WHERE Nama_barang LIKE %s OR Id_barang LIKE %s OR Harga_barang LIKE %s OR Stok_awal LIKE %s OR Barang_masuk LIKE %s OR Barang_keluar LIKE %s OR Stok_akhir LIKE %s", (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    result = cursorObject.fetchall()
    # Menampilkan data barang yang sesuai dengan kata kunci
    if result:
        print("Data barang yang ditemukan:")
        for x in result:
            print(x)
    else:
        print(f"Tidak ada data barang yang ditemukan dengan kata kunci '{keyword}'")

#fungsi pilihan menu
def show_menu():
    print("\n")
    print("=== APLIKASI DATABASE PYHTON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("----------------------")
    
    menu = input("Pilih Menu> ")
    print("\n")

    if menu == "1":
        insert_data()
    elif menu == "2":
        show_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        search_data()
    elif menu == "0":
        print("Keluar dari program...")
        exit()
    else:
        print("Input tidak valid, silakan pilih menu yang tersedia.")
        
if __name__ == "__main__":        
    while(True):
        show_menu()

#menutup koneksi database
db.close()


# In[ ]:




