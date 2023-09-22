# from flask import Flask, request, redirect, url_for, flash
# import os
# import subprocess
# import  secrets
# app = Flask(__name__)
# app.secret_key = secrets.token_hex(16) 
# UPLOAD_FOLDER = '../'  # 上层目录
# ALLOWED_EXTENSIONS = {'java'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # 检查是否有文件部分
#         if 'file' not in request.files:
#             flash('没有文件')
#             return redirect(request.url)
#         file = request.files['file']
#         # 如果用户没有选择文件，浏览器也可能会提交一个空文件
#         if file.filename == '':
#             flash('没有选择文件')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = 'Input.java'
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
            
#             # 调用code2seq.py进行预测
#             cmd = ["python3", "../code2seq.py", "--load", "../models/officemodel/models/java-large-model/model_iter52.release", "--predict"]
#             subprocess.run(cmd)
            
#             flash('文件已上传并进行预测')
#             return redirect(request.url)
#     return 
# import secrets

# if __name__ == '__main__':
#     app.run(debug=True)




#可以运行 但是很慢 
from flask import Flask, request, redirect, render_template, flash
import os
import subprocess
import secrets

app = Flask(__name__)
UPLOAD_FOLDER = '../'  # 上层目录
ALLOWED_EXTENSIONS = {'java'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = secrets.token_hex(16)  # 生成一个随机的密钥

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件部分
        if 'file' not in request.files:
            flash('没有文件')
            return redirect(request.url)
        file = request.files['file']
        # 如果用户没有选择文件，浏览器也可能会提交一个空文件
        if file.filename == '':
            flash('没有选择文件')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'Input.java'
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # 调用code2seq.py进行预测
            cmd = ["python3", "../code2seq.py", "--load", "../models/officemodel/models/java-large-model/model_iter52.release", "--predict"]
            result = subprocess.check_output(cmd, universal_newlines=True)
            
            return render_template('result.html', prediction=result)
    return render_template('upload.html')  # 这里返回上传页面的HTML内容

if __name__ == '__main__':
    app.run(debug=True)



# 加快版本
# app.py

# app.py

# from flask import Flask, request, render_template, flash, redirect, url_for
# import os
# import secrets
# from sys import path
# path.append('..')  # 添加上层目录到系统路径
# from c2sflask import Code2SeqModel

# app = Flask(__name__)
# UPLOAD_FOLDER = '../'  # 上层目录
# ALLOWED_EXTENSIONS = {'java'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = secrets.token_hex(16)  # 生成一个随机的密钥

# code2seq_model = Code2SeqModel(load_path="/home/luowangda/LDpacong/code2seq/code2seq/models/officemodel/models/java-large-model/model_iter52.release")

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # 检查是否有文件部分
#         if 'file' not in request.files:
#             flash('没有文件')
#             return redirect(request.url)
#         file = request.files['file']
#         # 如果用户没有选择文件，浏览器也可能会提交一个空文件
#         if file.filename == '':
#             flash('没有选择文件')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = 'Input.java'
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
            
#             # 使用Code2Seq模型进行预测
#             with open(filepath, 'r') as f:
#                 input_data = f.read()
#             prediction = code2seq_model.predict(input_data)
            
#             return render_template('result.html', prediction=prediction)
#     return render_template('upload.html')

# if __name__ == '__main__':
#     app.run(debug=True)
