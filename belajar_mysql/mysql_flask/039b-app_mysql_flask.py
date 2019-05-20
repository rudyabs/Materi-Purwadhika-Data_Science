from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'rudyabs'
app.config['MYSQL_PASSWORD'] = 'Kecapi48'
app.config['MYSQL_DB'] = 'tes_flask'

@app.route('/')
def home():
    return jsonify({'status': 'Welcome'})

@app.route('/data')
def data():
    x = mysql.connection.cursor()
    x.execute('select * from mytable')
    data = x.fetchall()
    print(data) #menghasilkan data tupple dari database
    print(type(data))
    # loop untuk merubah file tupple menjadi json

    semua_data =[]
    for i in range(len(data)):
        id = data[i][0]
        nama = data[i][1]
        usia = data[i][2]
        data_dict = {
            "id":id,
            "nama":nama,
            "usia":usia
        }
        semua_data.append(data_dict)
    print(semua_data)
    return jsonify(semua_data)

# membuat dynamic route - mengambil data dengan kriteria tertentu (id)
@app.route('/data/<string:id>') #bisa menggunakan <path:id>
def data_satuan(id):
    x = mysql.connection.cursor()
    x.execute(f'select * from mytable where id ={id}')
    # alternatif-> x.execute('select * from mytable where id =%s', (id) id)
    data = x.fetchall()
    print(data) #menghasilkan data tupple dari database
    print(type(data))
    # loop untuk merubah file tupple menjadi json
    semua_data =[]
    for i in range(len(data)):
        id = data[i][0]
        nama = data[i][1]
        usia = data[i][2]
        data_dict = {
            "id":id,
            "nama":nama,
            "usia":usia
        }
        semua_data.append(data_dict)
    print(semua_data)
    return jsonify(semua_data)


if __name__ == '__main__':
    app.run(debug = True)

