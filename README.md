# UTS-Python

Penjelasan Skrip 

Pada cell pertama terdapat skrip untuk membuat koneksi pada server data base serta untuk membuat database baru Bernama “db_V3922024”

import mysql.connector
db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = ""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_V3922024")


Pada cell kedua merupakan skrip untuk mengkoneksikan ke database “db_V3922024” dan skrip untuk membuat table Bernama “Stok_barang” yang terdiri dari kolom-kolom yang bernama Id_barang sebagai primary key, Nama_barang, Harga_barang, Stok_awal, Barang_masuk, Barang_keluar, dan Stok_akhir.

import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    passwd = "",
    database ="db_V3922024"
)

cursorObject = db.cursor()

cursorObject.execute("""CREATE TABLE Stok_barang (
                Id_barang VARCHAR(20) PRIMARY KEY,
                Nama_barang VARCHAR(100),
                Harga_barang INT,
                Stok_awal INT,
                Barang_masuk INT,
                Barang_keluar INT,
                Stok_akhir INT
                )""")

db.close()


Pada cell ketiga merupakan skrip untuk mengkoneksikan ke database “db_V3922024” serta untuk memanipulasi data dalam table “Stok_barang”

import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    passwd = "",
    database ="db_V3922024"
)

cursorObject = db.cursor()


Pertama terdapat fungsi untuk menambahkan data baru dalam table “Stok_barang”. Pengguna akan diminta untuk memasukkan inputan-inputan terkait data yang ada dalam table “Stok_barang”. Kemudian program akan memasukan data yang telah diinput kedalam database dengan menggunakan query INSERT INTO Stok_barang diikuti nama kolom dan valuenya. Setelah itu jika data berhasil ditambahkan maka program akan menampilkan “Data berhasil ditambahkan”

def insert_data():

    Id_barang = input("Masukkan ID Barang: ")
    Nama_barang = input("Masukkan Nama Barang: ")
    Harga_barang = int(input("Masukkan Harga Barang: "))
    Stok_awal = int(input("Masukkan Stok Awal Barang: "))
    Barang_masuk = int(input("Masukkan Jumlah Barang Masuk: "))
    Barang_keluar = int(input("Masukkan Jumlah Barang Keluar: "))
    Stok_akhir = Stok_awal + Barang_masuk - Barang_keluar
    
    sql = "INSERT INTO Stok_barang (Id_barang, Nama_barang, Harga_barang, Stok_awal, Barang_masuk, Barang_keluar, Stok_akhir) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_barang, Nama_barang, Harga_barang, Stok_awal, Barang_masuk, Barang_keluar, Stok_akhir)
    cursorObject.execute(sql, val)
    db.commit()
    print("Stok Akhir Barang: ", Stok_akhir)
    print(cursorObject.rowcount, "Data berhasil ditambahkan")


Kedua terdapat fungsi untuk menampilkan data yang ada dalam database dengan menggunakan query SELECT * FROM Stok_barang,

def show_data():
    
    cursorObject.execute("SELECT * FROM Stok_barang")
    result = cursorObject.fetchall()
    for x in result:
        print(x)


Ketiga terdapat fungsi untuk mengupdate atau edit data dalam database. Pertama program akan menampilkan seluruh data dalam databae dan pengguna akan diminta memasukkan id barang yang yang akan diubah. Serta pengguna juga akan diminta memasukkan data-data baru sesuai nama kolom jika ada kolom yang tidak ingin diubah maka boleh dikosongi sementara itu data-data lama sebelum diubah akan sisimpan pada variabel sementara yang berakhiran lama, lalu jika terdapat kolom yang akan diubah maka data baru dari inputan pengguna akan menggantikan data lama yang telah disimpan. Kemudian program akan melakukan update data dengan query UPDATE Stok_barang dan menset nilai pada setiap kolom sesuai dengan data yang tersimpan pada variabel sementara. Selanjutnya program akan menampilkan data dalam database yang telah dilakukan update data.

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


Kempat terdapat fungsi hapus delete data untuk menghapus data dari database. Disini pengguna akan diminta memasukan id barang yang ingin dihapus dan program akan menghapus data berdasarkan id barang yang diberikan dengan menggunakan query DELETE FROM stok_barang. Selanjutnya jika data telah berhasil dihapus maka program akan menampilkan “Data berhasil dihapus”.

def delete_data():
    
    Id_barang = input("Masukkan ID Barang yang Ingin Dihapus: ")
    sql = "DELETE FROM Stok_barang WHERE Id_barang = %s"
    val = (Id_barang,)
    cursorObject.execute(sql, val)
    db.commit()
    print(cursorObject.rowcount, "Data berhasil dihapus")



Kelima terdapat fungsi cari data berdasarkan keyword. Pertama pengguna diminta untuk memasukkan keyword data yang ingin dicari. Lalu program akan meampilkan data berdasarkan keyword yang telah diberikan dengan query SELECT * FROM Stok_barang WHERE Nama_barang ..LIKE ..keyword. kemudian jika data yang dicari berhasil ditemukan maka akan menampilkan "Data barang yang ditemukan" berserta datanya jika tidak ditemukan maka akan menampilkan “Tidak ada data barang yang ditemukan dengan kata kunci '{keyword}'"

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


Keenam terdapat fungsi pilihan menu. Disini program akan menampilkan beberapa pilihan menu untuk memanipulasi data, lalu pengguna akan diminta memasukan pilihan menu yang ingin dijalankan jika pengguna memilih menu 1 maka program akan memanggil fungsi insert_data, jika memilih menu 2 makan akan memanggil fungsi show_data, jika memilih menu 3 maka program akan memanggil fungsi update_data, jika pengguna memilih menu 4 maka akan memanggil fungsi delete_data, jika memilih menu 5 maka program akan memanggil fungsi search_data, jika pengguna memilih menu 0 maka  akan keluar dari program, dan jika menginputkan selain pilihan menu maka akan muncul "Input tidak valid, silakan pilih menu yang tersedia."

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


Skrip ini berfungsi untuk menjalankan fungsi show_menu jika file dijalankan sebagai program dan program akan terus berjalan sampai pengguna memilih opsi untuk keluar.        


if __name__ == "__main__":        
    while(True):
        show_menu()

db.close()
