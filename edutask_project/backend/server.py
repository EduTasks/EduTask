from flask import Flask, request, jsonify
from DaoServer import DaoServer

app = Flask(__name__)
dao = DaoServer()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = dao.login(username, password)
    
    if user:
        return jsonify({
            "msg": "Autenticació correcta",
            "coderesponse": "1",
            "data": user
        }), 200
    else:
        return jsonify({
            "msg": "Credencials incorrectes",
            "coderesponse": "0",
            "data": None
        }), 401

@app.route('/api/tasques', methods=['GET'])
def llistar_tasques():
    tasques = dao.get_tasques()
    return jsonify({
        "msg": f"S'han trobat {len(tasques)} tasques",
        "coderesponse": "1",
        "data": tasques
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)