from flask import Flask,  make_response, render_template,  send_file,  jsonify
from service import service
import helpers

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'
app.config['debug'] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["APPLICATION_ROOT"] = helpers.homeApi


@app.route(helpers.home, methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route(helpers.homeApi, methods=['POST', 'GET'])
def get_health():
    data = {'is_server_on': True, }
    return make_response(jsonify(data), 200)


@app.route(helpers.homeApi+'/file', methods=['POST'])
def upload():
    srv = service(app.config['UPLOAD_FOLDER'])
    srv.run()
    return srv.response()


@app.route(helpers.homeApi+'/download', methods=['GET'])
def download():
    return send_file(app.config['UPLOAD_FOLDER']+'\\out.csv', as_attachment=True)


if (__name__ == "__main__"):
    app.run(debug=True)
