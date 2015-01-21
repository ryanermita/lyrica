from lyrica import db, collection
from bson.json_util import dumps
from bson.objectid import ObjectId
import ast


# Parse mongo object to more 
# readable list of dict.
# Remove _id field and moved its
# value to id key.
def parse_mongoObj(jsn):
    jsn =ast.literal_eval(dumps(jsn))
    for i, v in enumerate(jsn):
        jsn[i]['id'] = jsn[i]['_id']['$oid']
        del jsn[i]['_id']

    return jsn

# For single data. convert list to 
# dictionary.
def to_dict(jsn):
    result = {}
    for d in jsn: result.update(d)
    return result

# Insert new lyrica, return newly added record.
def insert_lyrica(data):
    db[collection].insert(data)
    lyrica = db[collection].find(data)
    r = parse_mongoObj(lyrica)

    return to_dict(r)

# delete lyrica based on its id
def delete_lyrica(id):
    db[collection].remove({'_id': ObjectId(id)})

# update lyrica based on its id
# and return newly updated record.
def update_lyrica(id, data):
    db[collection].update({'_id': ObjectId(id)}, {'$set': data})
    lyrica = db[collection].find({'_id': ObjectId(id)})
    r = parse_mongoObj(lyrica)

    return to_dict(r)

# Get record in db, if id is present fetch single record.
# if id is None fetch all record.
def get_lyrica(id):
    lyrica = db[collection].find({'_id': ObjectId(id)})
    mongoObj = parse_mongoObj(lyrica)
    r = to_dict(mongoObj)

    if id is None:
        lyrica = db[collection].find()
        r = parse_mongoObj(lyrica)

    return r
