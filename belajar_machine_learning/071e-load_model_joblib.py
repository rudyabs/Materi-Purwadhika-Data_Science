from sklearn.externals import joblib
model = joblib.load('071-model_joblib')
print(model.predict([[10,2,200]]))