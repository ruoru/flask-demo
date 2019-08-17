from flask import Flask, request, render_template, jsonify
import json
# import os
import xlrd


app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        j_data = json.loads(request.data)
        return jsonify({
            'answer': j_data['a'] + j_data['b'],
            'questions': [j_data['question'], j_data['question']]
        })


# 限制上传的文件格式
ALLOWED_EXTENSIONS = ['xls', 'xlsx']


def allowe_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 修改文件名

# def change_filename(filename):
#     fileinfo = os.path.splitext(filename)
#     filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + \
#         str(uuid.uuid4().hex)+fileinfo[-1]
#     return filename


# 判断储存路径
FILE_DIR = '~/Desktop/aaaa'


# def explore_path():
#     if not os.path.exists(FILE_DIR):
#     os.makedirs(FILE_DIR)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        file = request.files['file']
        if file:
            file_read = file.read()  # 文件内容
            wb = xlrd.open_workbook(file_contents=file_read)
            table = wb.sheets()[0]
            # names = data.sheet_names()  # 返回book中所有工作表的名字
            # status = data.sheet_loaded(names[0])  # 检查sheet1是否导入完毕
            # file.save('~/Desktop/as.js')    #保存文件

            row_num = table.nrows  # 获取该sheet中的有效行数
            # ncols = table.ncols  # 获取该sheet中的有效列数

            table_data = []
            for i in range(1, row_num):
                row_value = table.row_values(i)
                row_data = {}
                for index, key in enumerate(table.row_values(0)):
                    row_data[key] = row_value[index]
                table_data.append(row_data)
            return jsonify({
                'data': table_data
            })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
