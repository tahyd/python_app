from flask import Flask,jsonify

from flask_jwt_extended import create_access_token,JWTManager, jwt_required,set_access_cookies
from flask_jwt_extended import get_jwt_identity
from app1 import app2
from app2 import app1
from app3 import app3
from loansapp import loansapp;
main_app = Flask(__name__);
main_app.config['Debug']= True
main_app.config['WTF_CSRF_ENABLED'] = False
main_app.register_blueprint(app1);
main_app.register_blueprint(app2);
main_app.register_blueprint(app3);
main_app.register_blueprint(loansapp);

main_app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" with something else!

# Here you can globally configure all the ways you want to allow JWTs to
# be sent to your web application. By default, this will be only headers.
main_app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
jwt = JWTManager(main_app)

@main_app.route('/token', methods=["POST"])
def create_token():
    print('Token')
    # Sending JWT as json 
  #  access_token = create_access_token(identity='krishna');
   # return jsonify(access_token=access_token);
   #sending JWT Via Cookie
    response= jsonify({"message":"Token sent successfully"});
    access_token = create_access_token(identity='krishna');
    set_access_cookies(response,access_token)
    return response;

@main_app.route("/welcome")
@jwt_required(locations=["headers"])
def sample():
    print(get_jwt_identity())
    return "Hello World  to Python Programing !";
@main_app.route("/hello1")
def helloword():
    return "Welcome To Jenkins"

if __name__ == '__main__':
    print('Main')
    main_app.run(debug=True,host=0.0.0.0,port=5000)
