from flask import Flask, render_template, request, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os #mengatur dimana path file kita ingin disimpan

app = Flask(__name__)
# untuk mengatur tempat dimana file disimpan
app.config['UPLOAD_FOLDER'] = './storage'


# Home route
@app.route('/')
def home():
    return render_template("033-tes.html")

# 404 error handler
@app.errorhandler(404)
def not_found404(error):
    return render_template('033b-404_error.html')

# upload route
@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['file']
    nama_file = secure_filename(data.filename)
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_file))
    # hanya untuk ngeprint
    print(data)
    print(nama_file)
    # redirect ke root baru saat selesai upload
    return redirect('/storage/' + nama_file) #jika mau langsung ngelihat pakai "return send_from directory('storage', nama_file)" 

# after upload = render static file buat root baru
@app.route('/storage/<path:path>')
def upload_success(path):
    return send_from_directory('storage', path)

# new route
@app.route('/new')
def new():
    return render_template('033c-new.html')
    
if __name__ == "__main__":
    app.run(debug = True)

