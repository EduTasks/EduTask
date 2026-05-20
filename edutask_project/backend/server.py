import os
from flask import Flask, request, jsonify
from DaoServer import DaoServer

app = Flask(__name__)
dao = DaoServer()

# Carpeta donde se guardarán físicamente los PDFs, Zips, etc.
UPLOAD_FOLDER = 'archivos_subidos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

@app.route('/api/login', methods=['POST'])
def login():
    # ... (Tu código de login se queda igual) ...
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = dao.login(username, password)
    if user:
        return jsonify({"msg": "Autenticació correcta", "coderesponse": "1", "data": user}), 200
    else:
        return jsonify({"msg": "Credencials incorrectes", "coderesponse": "0", "data": None}), 401

@app.route('/api/tasques', methods=['GET'])
def llistar_tasques():
    # ... (Tu código de listar tareas se queda igual) ...
    tasques = dao.get_tasques()
    return jsonify({"msg": f"S'han trobat {len(tasques)} tasques", "coderesponse": "1", "data": tasques}), 200

# --- NUEVA RUTA PARA RECIBIR ARCHIVOS ---
@app.route('/api/entregar', methods=['POST'])
def entregar_tasca():
    # Comprobamos que el cliente ha enviado un archivo
    if 'file' not in request.files:
        return jsonify({"msg": "No s'ha enviat cap arxiu", "coderesponse": "0"}), 400
    
    file = request.files['file']
    id_tarea = request.form.get('id_tarea')
    id_alumno = request.form.get('id_alumno')

    if file.filename == '':
        return jsonify({"msg": "Nom d'arxiu buit", "coderesponse": "0"}), 400

    # 1. Guardamos el archivo en el servidor
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # 2. Guardamos la ruta en MySQL
    exito = dao.crear_entrega(id_tarea, id_alumno, filepath)

    if exito:
        return jsonify({"msg": "Tasca lliurada correctament", "coderesponse": "1"}), 200
    else:
        return jsonify({"msg": "Error al guardar a la BBDD", "coderesponse": "0"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)