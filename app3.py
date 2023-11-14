from flask import Blueprint,render_template,url_for,redirect,request
import pickle
import json
app3 = Blueprint('app3',__name__);
@app3.route("/employee", methods=['POST'])
def readData():
    #data=request.get_json();
    data = request.form
    salary ={}
    salary['years'] = data['years']
    salary['expsal'] = getSalary(data['years']);
    json_sal = json.dumps(salary);
   # response  = app3.response_class(response=json_sal,status=200,mimetype='application/json')
    return json_sal,200




def getSalary(years):
   with open('model_pickle','rb') as f :
      m  = pickle.load(f);
      x= m.predict([[float(years)]])
      return x[0]