from flask import Flask
from flask_app.my_app.hello.views import hello
app = Flask(__name__)
app.register_blueprint(hello)
