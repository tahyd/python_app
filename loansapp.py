from flask import Blueprint
import pickle
from sklearn.preprocessing import StandardScaler
loansapp = Blueprint('loansapp',__name__,url_prefix="/loansapp")

@loansapp.route("/loans")
def getLoanInfo():
    with open('logistic_loan.pkl','rb') as f:
       scalar = StandardScaler();
       scalar.fit([[90,80]])
       data = scalar.transform([[90000,800000]])
       print(data[0,0])
       x = pickle.load(f);
    return "Loans App !"