from flask import Flask, request, jsonify, make_response, render_template, send_file
from appcore import AppCore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_114514'


# API
@app.route('/api/register', methods=['GET'])
def api_register():
    pass
