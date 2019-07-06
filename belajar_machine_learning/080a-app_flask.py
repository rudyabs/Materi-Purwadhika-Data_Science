from flask import Flask, render_template, request, url_for
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('080-home.html')

if __name__ == '__main__':
    model = joblib.load('080-logreg_deploy.joblib')
    app.run(debug=True)


    