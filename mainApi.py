from flask import Flask, Response, make_response, render_template, request, send_file, redirect, flash, jsonify
from serviceAPI import serviceAPI
import helpers

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'
app.config['debug'] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["APPLICATION_ROOT"] = helpers.homeApi


@app.route(helpers.home, methods=['POST', 'GET'])
def index():
    return render_template('index.ajax.html')


@app.route(helpers.homeApi, methods=['POST', 'GET'])
def root():
    data = {'is_server_on': True, }
    return make_response(jsonify(data), 200)


@app.route('/old', methods=['POST', 'GET'])
def old():
    return render_template('oldindex.html')


@app.route(helpers.homeApi+'/file', methods=['POST'])
def read():
    srv = serviceAPI(app.config['UPLOAD_FOLDER'])
    srv.run()
    return srv.response()


@app.route(helpers.homeApi+'/download', methods=['GET'])
def download():
    return send_file(app.config['UPLOAD_FOLDER']+'\\out.csv', as_attachment=True)


if (__name__ == "__main__"):
    app.run(debug=True)
