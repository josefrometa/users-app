from flask import Flask, jsonify
from flask_cors import CORS
from routes.user_list import user_list
from routes.user_email_search import user_email_search
from routes.user_name_and_email_search import user_bp
from routes.user_delete import user_delete
from routes.user_add import user_add

app = Flask(__name__)
CORS(app)


app.register_blueprint(user_email_search, url_prefix ='/user')
app.register_blueprint(user_list, url_prefix='/users')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(user_delete, url_prefix='/delete')
app.register_blueprint(user_add, url_prefix='/user') 


@app.route('/')
def index():
    return jsonify ({"data":"user-app"})

if __name__ == "__main__":
    app.run(debug=True)

