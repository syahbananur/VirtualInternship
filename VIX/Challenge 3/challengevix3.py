#Melakukan import mysql connector
import mysql.connector

#Melakukan percobaan koneksi
conn = mysql.connector.connect(
    host = 'localhost', user = 'root', password = 'MySQL#1234', database = 'perusahaan')

#Membuat object cursor sebagai penanda
cursor = conn.cursor()

#Deklarasi SQL QUery untuk memasukkan record ke DB (KARYAWAN)
insert_sql = (
    "INSERT INTO KARYAWAN (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)" 
    "VALUES (%s, %s, %s, %s, %s)"
)
values = ("Joko", "dwi", 25, "M", 50000)

try:
    #Eksekusi SQL Command
    cursor.execute(insert_sql, values)

    #Melakukan perubahan (commit) pada DB
    conn.commit()

except:
    #Roll Back apabila ada issue
    conn.rollback()

#Menutup Koneksi
conn.close()