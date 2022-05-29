from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'hi'


if (__name__ == "__main__"):
    app.run(debug=True)
