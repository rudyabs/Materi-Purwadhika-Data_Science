# saat python 
# pip install MySQL-connector-python

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# deklarasi database yang dipakai
@app.route('/data')
def data():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'rudyabs',
        passwd = 'Kecapi48',
        database = 'tes_flask'
    )
    x = mydb.cursor()
    x.execute('select * from mytable')
    data = x.fetchall()

    print(data)
    hasil_data = []
    for i in range(len(data)):
        id = data[i][0]
        nama = data[i][1]
        usia = data[i][2]
        hasil = {
            'id':id,
            'nama':nama,
            'usia':usia
        }
        hasil_data.append(hasil)
    return jsonify(hasil_data)

if __name__ == '__main__':
    app.run(debug = True)