from flask import Blueprint
import pickle
from sklearn.preprocessing import StandardScaler
loansapp = Blueprint('loansapp',__name__,url_prefix="/loansapp")
from flask import request

@loansapp.route("/loans",methods =["POST"])
def get_loan_info():
    loan_application = request.get_json();
    return isEligibleForLoan(loan_application)

def isEligibleForLoan(loan_application):
     scalar = StandardScaler();
     scalar.fit([[90,80]])
     data = scalar.transform([[4500,3000]])
     p1 =data[0,0];
     p2 = data[0,1];
     with open('logistic_loan.pkl','rb') as f:
       loans_model = pickle.load(f)
       pridiction_result =loans_model.predict([[1,1,1,1,p1,p2,1,2]])  
          
       return str(pridiction_result[0])