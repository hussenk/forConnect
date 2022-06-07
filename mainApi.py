from flask import Flask, render_template, request, send_file, redirect, flash, jsonify
from serviceV2 import serviceV2
import helpers

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'
app.config['debug'] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'



@app.route(helpers.homeApi, methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/old', methods=['POST', 'GET'])
def old():
    return render_template('oldindex.html')


@app.route('/file', methods=['GET', 'POST'])
def read():
    srv = serviceV2()
    if(srv.handelRequest() == False):
        flash('missing in handel Request', 'error')
        return redirect(helpers.homeApi)

    if(srv.handelForm() == False):
        flash('missing in form', 'error')
        return redirect(helpers.homeApi)

    srv.handelFile()
    srv.readHeaders()
    srv.deleteColumn()
    srv.setHeaders()
    srv.getNextColumn()
    srv.readRows()
    srv.replaceText()
    srv.createCSV(app.config['UPLOAD_FOLDER'])

    # return send_file(app.config['UPLOAD_FOLDER']+'\\out.csv', as_attachment=True)
    # return render_template('file.html')
    # return redirect(helpers.homeApi)


@app.route('/download', methods=['POST'])
def download():
    return send_file(app.config['UPLOAD_FOLDER']+'\\out.csv', as_attachment=True)


if (__name__ == "__main__"):
    app.run(debug=True)
