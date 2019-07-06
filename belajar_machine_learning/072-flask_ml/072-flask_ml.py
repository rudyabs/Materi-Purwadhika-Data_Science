from flask import Flask, redirect, render_template, url_for, jsonify,request
import joblib
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        'coef[0]': model.coef_[0],
        'coef[1]': model.coef_[1],
        'coef[2]': model.coef_[2],
        'intercept':model.intercept_
    })

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        body = request.json
        # urutan data yang didapat [['usia','kamar','luas']]
        
        usia = body['usia']
        kamar = body['kamar']
        luas = body['luas']
        prediksi = model.predict([[usia,kamar,luas]])

        return jsonify({
            'usia':usia,
            'kamar':kamar,
            'luas':luas,
            'status':'Anda sukses nge-POST',
            'prediksiharga':prediksi[0]
            })
    else:
        return jsonify({'status':'Anda tidak nge-POST'})

if __name__ == '__main__':
    model = joblib.load('071-model_joblib')
    app.run(debug=True)
