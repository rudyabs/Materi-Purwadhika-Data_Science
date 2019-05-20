from flask import Flask, request, jsonify
app = Flask(__name__)

# dictionaries
karyawan = [
    {"id": 1, "nama":"Andi", "job": "sales"},
    {"id": 2, "nama":"Budi", "job": "marketing"},
    {"id": 3, "nama":"Caca", "job": "finance"}
]

# home route
@app.route("/")
def home():
    return "Selamat Datang!"

# search?keyword= route
# search merupakan route
# keyword merupakan properti
# =... merupakan hal yg ingin di GET
# ?key=value&key=value
@app.route("/search")
def search():
    if 'keyword' in request.args:
        return request.args["keyword"]
    else:
        return "Hasil pencarian tidak ditemukan"
    # print(request.args) 
    # print(request.args["katakunci"])
    # print(request.args["lokasi"])
    return request.args["keyword"] + " " + request.args['lokasi']

# database karyawan
@app.route("/karyawan")
def cari_karyawan():
    # mencari data -> "id"
    if "id" in request.args:
        id = int(request.args["id"])
        if id < 1 or id > len(karyawan):
            return "Maaf data karyawan tidak ditemukan" 
        return jsonify(karyawan[id-1])
    # mencari data -> "nama"
    elif "nama" in request.args:
        return jsonify(karyawan)
    # mencari data -> "job"
    elif "job" in request.args:
        return jsonify(karyawan)
    else:
        return jsonify(karyawan)

if __name__ == "__main__":
    app.run(debug=True)