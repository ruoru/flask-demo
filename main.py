from flask import Flask
from app.home import home
from app.add import add
from app.upload import upload

app = Flask(__name__, static_url_path='')

app.register_blueprint(home)
app.register_blueprint(add)
app.register_blueprint(upload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
