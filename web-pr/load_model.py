import pickle as pk
import pandas as pd

model = pk.load(open("Finalized_model.sav", 'rb'))

def predict_model(data):
    df = pd.DataFrame(data, index=[0])
    return model.predict(df)[0][0]
    