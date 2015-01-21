from flask import jsonify, request
from lyrica import lyrica, db

# Test page, to check if app is running.
@lyrica.route('/')
@lyrica.route('/index')
def index():
    return jsonify({"test": True})

# GET 
@lyrica.route('/v1/api/lyrica', methods=['GET'])
@lyrica.route('/v1/api/lyrica/<id>', methods=['GET'])
def get_lyrica(id=None):
    lyrica = helpers.get_lyrica(id)
    r = {
            "success": True,
            "lyrica": lyrica,
        }
    return jsonify(r)

# DELETE 
@lyrica.route('/v1/api/lyrica/<id>', methods=['DELETE'])
def delete_lyrica(id=None):
    r = {'success': False, 'lyrica': {}}

    if id is not None:
        lyrica = helpers.delete_lyrica(id)
        r['success'] = True

    return jsonify(r)

# POST 
@lyrica.route('/v1/api/lyrica', methods=['POST'])
def insert_lyrica(id=None):
    data = request.get_json(force=True)

    lyrica = helpers.insert_lyrica(data)
    r = {
            "success": True,
            "lyrica": lyrica,
        }

    return jsonify(r)

# UPDATE 
@lyrica.route('/v1/api/lyrica/<id>', methods=['PUT'])
def update_lyrica(id=None):
    data = request.get_json(force=True)

    lyrica = helpers.update_lyrica(id, data)
    r = {
            "success": True,
            "lyrica": lyrica,
        }

    return jsonify(r)
