from flask import Blueprint, request, render_template, jsonify
import json

add = Blueprint('add', __name__)


@add.route('/add', methods=['GET', 'POST'])
def add_page():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        j_data = json.loads(request.data)
        return jsonify({
            'answer': j_data['a'] + j_data['b'],
            'questions': [j_data['question'], j_data['question']]
        })
