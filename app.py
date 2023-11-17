from flask import Flask
from app1 import app2
from app2 import app1
from app3 import app3
main_app = Flask(__name__);
main_app.config['Debug']= True
main_app.register_blueprint(app1);
main_app.register_blueprint(app2);
main_app.register_blueprint(app3);
@main_app.route("/welcome")
def sample():
    return "Hello World  to Python Programing !";

@main_app.route("/hello1")
def helloword():
    return "Welcome To Jenkins"

if __name__ == '__main__':
    print('Main')
    main_app.run(port=5000)