import sqlite3

db = sqlite3.connect("visageimage.db")
print(db.execute('SELECT pk_id_img FROM IMAGENES  WHERE URL = ?', (r'static\uploaded_img\cacahuate.jpg',)).fetchone()[0]) 

lista = []
for i in lista:
    print(i)