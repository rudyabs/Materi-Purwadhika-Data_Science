# Load with pickle
import pickle

with open('071-model_pickle.pkl','rb') as filesaya:
    model = pickle.load(filesaya)

print(model.predict([[10,2,200]]))