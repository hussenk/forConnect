from operator import imod
from flask import Flask, render_template, request, url_for, redirect
from serves import serves
app = Flask(__name__)

srv = serves()

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/file', methods=['GET','POST'])
def read():
    srv.handelErrorUpload()

    if request.form.get('dColumnsCB') == 'on':
        srv.deleteColumn()

    if request.form.get('newHeadersCB') == 'on':
        srv.setNewHeaders()
    


    return 'file'

if (__name__ == "__main__"):
    app.run(debug=True)
