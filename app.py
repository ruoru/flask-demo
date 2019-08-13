from flask import Flask, request, render_template
import json

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
  j_data = json.loads(request.data)
  return json.dumps({ 'data': j_data['a'] + j_data['b'] })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)