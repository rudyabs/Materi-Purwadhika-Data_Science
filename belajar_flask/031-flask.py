# Flask dan django
# untuk membuat back-end server
# digunakan untuk menyediakan data yg digunakan user

# install package: python -m pip install flask
# version: flask --version

# ===========================================================
# pengaplikasian flask

from flask import Flask, render_template, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('031-test_server.html')

# data karyawan
karyawan = [
    {'id': 1, 'nama': 'Andi', 'usia':20},
    {'id': 2, 'nama': 'Budi', 'usia':30},
    {'id': 3, 'nama': 'Caca', 'usia':40},
    {'id': 4, 'nama': 'Dodo', 'usia':50},
    {'id': 5, 'nama': 'Ela', 'usia':60}
]
# 404 error handler
@app.errorhandler(404)
def tidak_ditemukan(ngehang):
    return make_response(
        render_template('031-error.html')
    )

# fixed route 
@app.route('/data')
def data():
    return jsonify(karyawan)

# dynamic route
@app.route('/data/<int:id>')
def user_id(id): 
    if id < 1 or id > len(karyawan):
        abort(404) # 404 error message
    else:
        return jsonify(karyawan[id-1]) 

# untuk mengambil variable diluar route
profilku = {
    'nama': 'Gogon Gegono',
    'usia': 51
}

@app.route('/about')
def about():
    return render_template(
        '031-about.html',
        profil = profilku
    )

@app.route('/tes', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def tes():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        pesan = request.json
        print(pesan['nama']) #hanya untuk mengecek data yg dimasukan
        return 'Pesan yang anda kirim = ' + pesan['nama']
    else:
        return 'Anda tidak nge-GET ataupun nge-POST'

# untuk mengambil dr dalam root

# @app.route('/about')
# def about():
#     nama = "Budi Susewo"
#     usia = 32
#     return render_template(
#         '031-about.html',
#         profil = {
#             'nama': nama,
#             'usia': usia
#         }
#         )
        
# bisa juga dimasukan diluar root

if __name__ == '__main__':
    app.run(debug = True) #debug digunakan agar server tidak perlu dimatikan saat ada perubahan


# untuk mengakses server, gunakan link untuk GET atau localhost
# localhost:5000 
# ==================================================================================================

