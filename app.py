# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Customer import Customer
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_Customer(data:Customer):
    data = data.dict()
    CreditScore=data['CreditScore']
    Gender=data['Gender']
    Age =data['Age']
    Tenure=data['Tenure']
    Balance=data['Balance']
    NumOfProducts=data['NumOfProducts']
    HasCrCard =data['HasCrCard']
    IsActiveMember=data['IsActiveMember']
    EstimatedSalary = data['EstimatedSalary']

   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[	CreditScore	,Gender	,Age,	Tenure,	Balance	,NumOfProducts,	HasCrCard,	IsActiveMember	,EstimatedSalary]])
    if(prediction[0]>0.5):
        prediction="Customer will churn"
    else:
        prediction="Customer will not churn"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)