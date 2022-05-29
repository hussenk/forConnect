from operator import imod
from flask import Flask, render_template, request, url_for, redirect
from serves import serves
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/file', methods=['GET','POST'])
def read():
    srv = serves()

    srv.handelErrorUpload()

    srv.loadFile()

    if request.form.get('dColumnsCB') == 'on':
        srv.deleteColumn()

    srv.saveCsv()

    return 'file'

if (__name__ == "__main__"):
    app.run(debug=True)
