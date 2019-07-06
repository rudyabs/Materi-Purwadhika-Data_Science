from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Home/index route
@app.route("/")
def index():
    return render_template('080b-welcome.html')

# Post to titanic model 6
@app.route('/titanic6',methods = ['GET','POST'])
def titanic6():
    if request.method == 'POST':
        body = request.json

        sex = body['sex'] # female = 0, male = 1
        age = body['age']
        sibsp = body['sibsp']
        parch = body['parch']
        pclass = body['pclass']
        fare = body['fare']


        # [ 0.    1.    0.    1.    0.    3.   22.    1.    0.    7.25  1.    0.  ]
        # female male child man woman pclass age sibsp par fare adultM alone
        
        if int(sex) == 0:
                if int(age) < 15:
                        female = 1
                        male = 0
                        child = 1
                        man = 0
                        woman = 0
                        adultman = 0
                else:
                        female = 1
                        male = 0
                        child = 0
                        man = 0
                        woman = 0  
                        adultman = 0     
        else:
                if int(age) > 15:
                        female = 0
                        male = 1
                        child = 1
                        man = 0
                        woman = 0
                        adultman = 0
                else:
                        female = 0
                        male = 1
                        child = 0
                        man = 1
                        woman = 0
                        adultman = 1  
        if int(sibsp) == 0 and int(parch) == 0:
                alone = 1
        else:
                alone = 0 
  
        prediksi = model.predict([[
                        female,male,child,man,woman,pclass,age,sibsp,parch,fare,adultman,alone
                        ]])

        # print(body['message'])
        # print(jsonify(body['message']))
        return jsonify({
                '0response':'POST  Sukses',
                'female' : female,
                'male' : male,
                'child' : child,
                'man' : man,
                'woman' : woman,
                'pclass' : pclass,
                'age' : age,
                'sibsp' : sibsp,
                'parch' : parch,
                'fare' : fare,
                'adultman' : adultman,
                'alone' : alone,
                'zprediksi': int(prediksi)
        })

# Post to titanic model 12
@app.route('/titanic12', methods = ['GET', 'POST'])
def titanic12():
    if request.method == 'POST':
        body = request.json
        
        # [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
        # fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone
        female = body['female']
        male = body['male']
        child = body['child']
        man = body['man']
        woman = body['woman']
        pclass = body['pclass']
        age = body['age']
        sibsp = body['sibsp']
        parch = body['parch']
        fare = body['fare']
        adultman = body['adultman']
        alone = body['alone']
        prediksi = model.predict([[
            female, male, child, man, woman, pclass, age, 
            sibsp, parch, fare, adultman, alone
        ]])[0]

        print(prediksi)
        return jsonify({
            '0response' : 'POST successful!', 
            'female' : female,
            'male' : male,
            'child' : child,
            'man' : man,
            'woman' : woman,
            'pclass' : pclass,
            'age' : age,
            'sibsp' : sibsp,
            'parch' : parch,
            'fare' : fare,
            'adultman' : adultman,
            'alone' : alone,
            'zPREDIKSI': int(prediksi)
})

# prediksi route
@app.route('/prediksi')
def prediksi():
        return render_template('080b-prediksi.html')

# result page
@app.route('/hasil', methods = ['GET', 'POST'])
def hasil():
    if request.method == 'POST':
        sex = int(request.form['sex'])
        age = int(request.form['age'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        pclass = int(request.form['pclass'])
        fare = int(request.form['fare'])

        if int(sex) == 0:
            if int(age) < 15:
                female = 1; male = 0; child = 1 
                man = 0; woman = 0; adultman = 0
            else:
                female = 1; male = 0; child = 0 
                man = 0; woman = 1; adultman = 0
        else:
            if int(age) < 15:
                female = 0; male = 1; child = 1 
                man = 0; woman = 0; adultman = 0
            else:
                female = 0; male = 1; child = 0 
                man = 1; woman = 0; adultman = 1
        
        if int(sibsp) == 0 and int(parch) == 0:
            alone = 1
        else:
            alone = 0

        # [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
        # fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone
        prediksi = model.predict([[
            female, male, child, man, woman, pclass, age, 
            sibsp, parch, fare, adultman, alone
        ]])[0]

        if int(prediksi) == 0:
                kesimpulan = 'YOU DIED'
        else:
                kesimpulan = 'Next stop, Final Destination'

        hasil = {
            'female': female, 'male': male, 'child': child, 
            'man': man, 'woman': woman, 'pclass': pclass, 
            'age': age, 'sibsp': sibsp, 'parch': parch, 
            'fare': fare, 'adultman': adultman, 'alone': alone,
            'PREDIKSI': kesimpulan
        }
        return render_template('080b-hasil.html', hasil=hasil)

if __name__=="__main__":
    model = joblib.load("080-logreg_deploy.joblib")
    app.run(debug=True, port=1234)