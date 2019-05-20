from flask import Flask, render_template
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template("033-tes.html")
# 404 error handler
@app.errorhandler(404)
def not_found404(error):
    return render_template('033b-404_error.html')

# new route
@app.route('/new')
def new():
    return render_template('033c-new.html')
    
if __name__ == "__main__":
    app.run(debug = True)