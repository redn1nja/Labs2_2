"""Web application"""
# import json
# import urllib
from flask import Flask, request, render_template
# import uvicorn
import mapper

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'POST':
        if request.form.get('action'):
            val = request.form.get('fname')
            return maps(val)
    return render_template('intro.html')

# @app.route('/tree', methods=['GET', 'POST'])
# def index():
#     # if request.method =='GET':
#     #     return render_template('intro.html')


@app.route('/map', methods=['POST', 'GET'])
def maps(acc):
    mapper.main(acc)
    return render_template('map.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
