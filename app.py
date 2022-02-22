import time

import tarantool

from flask import Flask, request, jsonify, abort

app = Flask(__name__)
storage = {}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/kv', methods=['POST'])
def add():
    request_data = request.get_json()
    key = request_data["key"]
    value = request_data["value"]
    if tester.select(key):
        abort(409)
    else:
        if isinstance(value, dict):
            tester.insert((key, value))
            return 'Created', 201
        else:
            abort(400)


@app.route('/kv/<id>', methods=['PUT'])
def update(id):
    request_data = request.get_json()
    value = request_data["value"]
    if not tester.select(id):
        abort(404)
    else:
        if isinstance(value, dict):
            tester.replace((id, value))
            return 'Ok', 200
        else:
            abort(400)


@app.route('/kv/<id>', methods=['GET'])
def get(id):
    if not tester.select(id):
        abort(404)
    else:
        result = tester.select(id)
        return jsonify({id: result[0][1]}), 200


@app.route('/kv/<id>', methods=['DELETE'])
def delete(id):
    if not tester.select(id):
        abort(404)
    else:
        tester.delete(id)
        return 'Not Content', 204


connection = tarantool.connect("tarantool", 3301, password='pass')
tester = connection.space('tester')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
