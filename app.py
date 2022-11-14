from flask import Flask, Request, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc
from tablas import db
from flask_cors import CORS, cross_origin
from logging import exception
from tablas import db, usuario, cliente, producto, comuna, compra

#instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_tienda.db'
db.init_app(app)
Migrate(app, db)

# Creamos la ruta por defecto para saber si mi app esta funcionado
# ejecutamos el comando en la consola: python app.py o python3 app.py y revisamos nuestro navegador
@app.route('/')
def index ():
    return 'Hola mundo'



#############################
# métodos.
#############################
# Para consultar todos los usuarios.
@app.route('/usuarios/', methods=['GET'])
def getUsuarios():
    try:
        usuarios = usuario.query.all()
        return jsonify([usuario.serialize() for usuario in usuarios])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#para consultar por los clientes.
@app.route('/clientes/', methods=['GET'])
def getclientes ():
    try:
        clientes = cliente.query.all()
        return jsonify([cliente.serialize() for cliente in clientes])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Para consultar un cliente por su id.

@app.route('/clientes/<rut>', methods=['GET'])
def getcliente (rut):
    try:
        clientes = cliente.query.get(rut)
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404
        else:
            return jsonify(clientes.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#para consultar por todos los productos.
@app.route('/productos', methods=['GET'])
def getproductos ():
    try:
        productos = producto.query.all()
        return jsonify([producto.serialize() for producto in productos])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Para consultar un producto por su id.
@app.route('/productos/<id_producto>', methods=['GET'])
def getproducto (id_producto):
    try:
        productos = producto.query.get(id_producto)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404
        else:
            return jsonify(productos.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Para consultar la lista de comunas.
@app.route('/comunas', methods=['GET'])
def getcomunas ():
    try:
        comunas = comuna.query.all()
        return jsonify([comuna.serialize() for comuna in comunas])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#consultar por una comuna por su id.
@app.route('/comunas/<id_comuna>', methods=['GET'])
def getcomuna(id_comuna):
    try:
        comunas = comuna.query.get(id_comuna)
        if not comuna:
            return jsonify({"error": "Comuna no encontrada"}), 404
        else:
            return jsonify(comunas.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
