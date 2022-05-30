from operator import imod
from flask import Flask, render_template, request, url_for, redirect
from service import service
import helpers
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'
app.config['debug'] = True


@app.route(helpers.home, methods=['POST', 'GET'])
def index():
    return render_template('index.html')





@app.route('/file', methods=['GET', 'POST'])
def read():
    srv = service()

    try:
        if(srv.handelErrorUpload() == False):
            return redirect(helpers.home)
    except:
        print('error handelErrorUpload')
        return redirect(helpers.home)

    try:
        srv.getForm()
    except:
        print('error getForm')
        return redirect(helpers.home)

    srv.setDirectory(app.config['UPLOAD_FOLDER'])

    try:
        srv.loadFile()
    except:
        print('error loadfile')
        return redirect(helpers.home)

    try:
        srv.setHeaders()
    except:
        print('error setHeaders')
        return redirect(helpers.home)
    try:
        srv.readRows()
    except:
        print('error readRows')
        return redirect(helpers.home)

    if request.form.get('dColumnsCB') == 'on':
        print('delete')
        srv.deleteColumn()

    try:
        srv.saveCsv()
    except:
        print('error saveCsv')
        return redirect(helpers.home)

    return 'file'


if (__name__ == "__main__"):
    app.run(debug=True)
