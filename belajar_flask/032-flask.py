from flask import Flask, send_from_directory, render_template, request, redirect, url_for
app = Flask(__name__, static_url_path='')

data = {
    "nama": "Andi",
    "pwd": "1234" 
}

# Home route
@app.route('/')
def home():
    return '<h1> Welcome to My Personal Web Server</h1>'

# render temlplate.html
@app.route('/signup')
def html_signup():
    return render_template('html_signup.html')

@app.route('/login')
def html_login():
    return render_template('html_login.html')

# POST route
@app.route('/post', methods=['POST'])
def post():
    nam = request.form['Nama']
    pwd = request.form['Pass']
    print('Nama :', nam, 'Pass :', pwd )
    # if nam = data['nama'] and pwd =:
    return redirect(url_for('sukses', nama = nam)) #"sukses" terhubung 

# redirect : butuh import "redirect", "url_form"
@app.route('/sukses/<string:nama>') 
def sukses(nama):
    return '<h1>Selamat datang ' + nama + '</h1>'

# Untuk file yang di post yaitu JSON
    # file_request = request.json #butuh import "request"
    # print('File sudah ter-POST : ' + file_request["nama"] + file_request["pass"]) #hanya untuk melihat file hasil
    # return "File sudah ter-POST : " + file_request["nama"] + file_request["pass"]
   

# render static file
@app.route('/images/<path:x>') #path = nama route
def static_file(x): #butuh import send_from_directory
    return send_from_directory('images', x) #nama folder

# 404 route
@app.errorhandler(404)
def error_404(error):
    return '<h1>Error: 404 Not Found</h1>'

if __name__ == '__main__':
    app.run(debug = True)