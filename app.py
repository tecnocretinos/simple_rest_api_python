import random
from flask import Flask, json, jsonify, request

app = Flask(__name__)

dummy_json = {
    "nohlkjnknlkj": {   
        "id": "nohlkjnknlkj",
        "name": "Elon Musk",
        "phone_number" : 3133007011,
        "address": "Mars",
        "iluminati": True
    },
    "asdasdha": {
        "id": "asdasdha",
        "name": "Steven Trabajo",
        "phone_number" : 3114005392,
        "address": "iCloud",
        "iluminati": False
    }
}

@app.route('/users/<id>', methods=['GET'])
def UserById(id):
    if request.method == 'GET':
        return jsonify(dummy_json[id])


@app.route('/users/', methods=['GET','POST', 'PUT', 'DELETE'])
def Users():
    if request.method == 'GET':
        return jsonify(dummy_json)

    elif request.method == 'POST':
        params = request.json
        id_hash = get_short_hash()
        params["id"] = id_hash
        dummy_json[id_hash] = params
        return jsonify(params)

    elif request.method == 'PUT':
        params = request.json

        if(params['id'] in dummy_json.keys()):
            dummy_json[params['id']] = params
            return jsonify(dummy_json)
        else:
            id_hash = get_short_hash()
            params.id = id_hash
            dummy_json[id_hash] = params
            return jsonify(params)

    elif request.method == 'DELETE':
        delete_id = request.args.get('id')
        dummy_json.pop(delete_id)
        return jsonify(dummy_json)

def get_short_hash():
    hash = hex(random.getrandbits(128))[2:-1]
    return hash[:10]

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    