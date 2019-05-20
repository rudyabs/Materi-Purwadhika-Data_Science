from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

# menggunakan flask_mysqldb

app =Flask(__name__)
MySQL = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app. config['MYSQL_USER'] = 'rudyabs'
app.config['MYSQL_PASSWORD'] = 'Kecapi48'
app.config['MYSQL_DB'] = 'tes_flask'

# home route
@app.route('/')
def home():
    return '<h1>Welcome!</h1>'

# route GET & POST data
@app.route('/dataku', methods=['GET', 'POST'])
def dataku():
    if request.method == 'GET':
        x = MySQL.connection.cursor()
        jumlah_data = x.execute('select * from mytable')
        print(jumlah_data)
        if jumlah_data > 0:
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
        else:
            return jsonify({'status': 'Tidak ada data'})
    else:
        # # mengambil body.request dari client 
        # # Jika menggunakan request.json
        # body = request.json
        # nama = body['nama']
        # usia = body['usia']

        # menggunakan html
        nama = request.form['nama_cpns']
        usia = request.form['usia_cpns']
        # post dan memasukan data ke database
        x = MySQL.connection.cursor()
        x.execute('insert into mytable (nama, usia) values (%s, %s)', (nama,usia))
        MySQL.connection.commit()
        return jsonify({'status': 'Anda nge-POST'})

# formulir
@app.route('/formulir')
def formulir():
     return render_template('040-formulir.html')

# active server
if __name__ == '__main__':
    app.run(debug=True) 