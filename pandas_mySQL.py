import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = '....',
    passwd = '.....',
    database = 'ptabc'
)

#MENAMPILKAN DATA 
c = db.cursor()
c = db.cursor(dictionary=True) #mengubah database dalam bentuk dictionary
query = 'select * from karyawan' #query atau perintah untuk menjalankan mysql
c.execute(query)
out = c.fetchall()

#MEMBUAT DATAFRAME
df = pd.DataFrame(out)
print(df)