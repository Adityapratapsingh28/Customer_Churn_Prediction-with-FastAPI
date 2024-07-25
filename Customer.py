from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Customer(BaseModel):
    CreditScore : int
    Gender : int
    Age : int
    Tenure : int
    Balance : float
    NumOfProducts : int
    HasCrCard  : int
    IsActiveMember : int
    EstimatedSalary : float