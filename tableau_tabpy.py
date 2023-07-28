import pickle
import pandas as pd
import numpy as np
from tabpy.tabpy_tools.client import Client
model = pickle.load(open('C:/Users/USER/Documents/ZHP/server/final_model.pickle', 'rb'))
X = pd.read_pickle("C:/Users/USER/Documents/ZHP/server/X.pkl")
#print(X)

def predict_price(city, total_sqft, bathrooms, bedrooms):
    loc_index = np.where(X.columns == city)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = total_sqft
    x[1] = bathrooms
    x[2] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1

    return [model.predict([x])[0]]  # Return as a list

#print(predict_price('Gilbert',4000,1,3))
'''
def predict_price(_arg1,_arg2,_arg3,_arg4):
    loc_index = np.where(X.columns==_arg1)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = _arg2
    x[1] = _arg3
    x[2] = _arg4
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0].tolist()
'''

client = Client('http://localhost:9004/')

client.deploy('predict_price',
predict_price,
'Returns prediction of house price in any particular area'
, override = True)




'''
def Profitability_Prediction(_arg1, _arg2, _arg3, _arg4, _arg5, _arg6):    
input_data = np.column_stack([_arg1, _arg2, _arg3, _arg4, _arg5, _arg6])
X = pd.DataFrame(input_data,columns=['Area','Age','Type','Capacity_Score',
'Food_Diversity_Score','Price_Range'])
result = model.predict(encoder.transform(X))
return result.tolist()
'''