from flask import jsonify, request
from lyrica import lyrica, db

# Test page, to check if app is running.
@lyrica.route('/')
@lyrica.route('/index')
def index():
    return jsonify({"test": True})
