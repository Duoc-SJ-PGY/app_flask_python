from flask import Flask, Request, jsonify, request
from flask_migrate import Migrate
from sqlalchemy import desc
from tablas import db
from flask_cors import CORS, cross_origin
from logging import exception
from tablas import db, usuario, cliente, producto, comuna, compra, ubicacion
from tablas import categorias, favoritos, info_pago, mis_compras, direcciones


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


#para consultar por usuario por su id.
@app.route('/usuarios/<user>', methods=['GET'])
def getusuario(user):
    try:
        usuarios = usuario.query.get(user)
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404
        else:
            return jsonify(usuarios.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#para crear un usuario en la BD.
@app.route('/usuarios', methods=['POST'])
def createUsuario():
    try:
        user = usuario()
        user.user = request.json.get('usuario')
        user.password = request.json.get('password')
        usuario.save(user)
        return jsonify(user.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#para guardar una ubicación.
@app.route('/ubicaciones', methods=['POST'])
def createUbicacion():
    try:
        ubi = ubicacion()
        ubi.id_ubicacion = request.json.get('id_ubicacion')
        ubi.latitud = request.json.get('latitud')
        ubi.longitud = request.json.get('longitud')
        ubicacion.save(ubi)
        return jsonify(ubi.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#para consultar una ubicación por su id.
@app.route('/ubicaciones/<id_ubicacion>', methods=['GET'])
def getUbicacion(id_ubicacion):
    try:
        ubicaciones = ubicacion.query.get(id_ubicacion)
        if not ubicacion:
            return jsonify({"error": "Ubicación no encontrada"}), 404
        else:
            return jsonify(ubicaciones.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#para consultar por una categoria.
@app.route('/categorias/<id_categoria>', methods=['GET'])
def getCategorias(id_categoria):
    try:
        cate = categorias.query.get(id_categoria)
        if not cate:
            return jsonify({"error": "Categoria no encontrada"}), 404
        else:
            return jsonify(categorias.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#Para guardar en favoritos.
@app.route('/favoritos', methods=['POST'])
def addFavoritos():
    try:
        fav = favoritos()
        fav.id = request.json.get('id')
        fav.id_producto = request.json.get('id_producto')
        
        favoritos.save(fav)
        return jsonify(fav.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Para consultar por favoritos.
@app.route('/favoritos/<id>', methods=['GET'])
def getFavoritos(id):
    try:
        fav = favoritos.query.get(id)
        if not fav:
            return jsonify({"error": "Favorito no encontrado"}), 404
        else:
            return jsonify(fav.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#para guardar los datos de pago del usuario.
@app.route('/infopagos', methods=['POST'])
def addInfoPago():
    try:
        info = info_pago()
        info.correlativo = request.json.get('correlativo')
        info.tipo_documento = request.json.get('tipo_documento')
        info.medio_pago = request.json.get('medio_pago')
        info.cuotas = request.json.get('cuotas')
              
        info_pago.save(info)
        return jsonify(info.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#para consultar por información del pago.
@app.route('/infopagos/<correlativo>', methods=['GET'])
def getInfoPago(correlativo):
    try:
        info = info_pago.query.get(correlativo)
        if not info:
            return jsonify({"error": "Información de pago no encontrada"}), 404
        else:
            return jsonify(info.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#Para consultar mis_compras.
@app.route('/mis_compras/<id>', methods=['GET'])
def getmiscompras(id):
    try:
        miscompras = mis_compras.query.get(id)
        if not miscompras:
            return jsonify({"error": "Compra no encontrada"}), 404
        else:
            return jsonify(miscompras.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Para guardar mis_compras.
@app.route('/mis_compras', methods=['POST'])
def addmiscompras():
    try:
        miscompras = mis_compras()
        miscompras.id = request.json.get('id')
        miscompras.id_compra = request.json.get('id_compra')
        miscompras.id_producto = request.json.get('id_producto')
        miscompras.rut = request.json.get('rut')
        miscompras.correlativo = request.json.get('correlativo')
        
        mis_compras.save(miscompras)
        return jsonify(miscompras.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#para guardar mis direcciones
@app.route('/mis_direcciones', methods=['POST'])
def addmisdirecciones():
    try:
        dir = direcciones()
        dir.id = request.json.get('id')
        dir.rut = request.json.get('rut')
        dir.id_comuna = request.json.get('id_comuna')
        dir.id_provincia = request.json.get('id_provincia')
        dir.id_ubicacion = request.json.get('id_ubicacion')
        
        direcciones.save(dir)
        return jsonify(dir.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#para consultar mis direcciones
@app.route('/mis_direcciones/<id>', methods=['GET'])
def getdirecciones(id):
    try:
        dir = direcciones.query.get(id)
        if not dir:
            return jsonify({"error": "Dirección no encontrada"}), 404
        else:
            return jsonify(dir.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#Para guardar las compras.
@app.route('/compras', methods=['POST'])
def addcompras():
    try:
        comp = compra()
        comp.id_comp = request.json.get('id_comp')
        comp.rut = request.json.get('rut')
        comp.id_prod = request.json.get('id_producto')
        comp.fecha_compra = request.json.get('fecha_compra')
        comp.fecha_entrega = request.json.get('fecha_entrega')
        comp.cantidad = request.json.get('cantidad')
        comp.precio = request.json.get('precio')
        comp.foto_producto = request.json.get('foto_producto')
        comp.nombre_producto = request.json.get('nombre_producto')
        comp.valor_envio = request.json.get('valor_envio')
                
        compra.save(comp)
        return jsonify(comp.serialize()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Para consultar las compras.
@app.route('/compras/<id_comp>', methods=['GET'])
def getcompras(id_comp):
    try:
        comp = compra.query.get(id_comp)
        if not comp:
            return jsonify({"error": "Compra no encontrada"}), 404
        else:
            return jsonify(comp.serialize()),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





if __name__ == '__main__':
    app.run(port=5000, debug=True)
