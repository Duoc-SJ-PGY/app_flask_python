from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Column
from sqlalchemy.orm import relationship
db = SQLAlchemy()

#creación de tabla de usuario para almacenar las credenciales
class usuario (db.Model):
    __tablename__ = 'usuario'
    user = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(10), primary_key=True)
    
    def serialize(self):
        return {
            "user": self.user,
            "password": self.password
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creación de tabla de Ubicación para almacenar las coordenadas
class ubicacion (db.Model):
    __tablename__ = 'ubicacion'
    id_ubicacion = db.Column(db.Integer, primary_key=True)
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)
    #user = db.Column(db.String(30), ForeignKey('usuario.user'))
    #usuario = relationship('usuario')
    
    def serialize(self):
        return {
            "id_ubicacion": self.id_ubicacion,
            "latitud": self.latitud,
            "longitud": self.longitud,
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creación de tabla categorias para almacenar las categorias de los productos
class categorias (db.Model):
    __tablename__ = 'categorias'
    id_categoria = db.Column(db.Integer, primary_key=True)
    desc_categoria = db.Column(db.String(30))
    id_producto = db.Column(db.Integer, ForeignKey('producto.id_producto'))
    FK_producto_categoria = relationship('producto')
    
    def serialize(self):
        return {
            "id_categoria": self.id_categoria,
            "nombre_categoria": self.desc_categoria,
            "id_producto": self.id_producto
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creación tabla favoritos para almacenar los productos favoritos de los usuarios
class favoritos (db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, ForeignKey('producto.id_producto'))
    FK_favoritos_producto = relationship('producto')
    
    def serialize(self):
        return {
            "id_producto": self.id_producto,
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creación de tabla producto para almacenar los productos
class producto (db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(10))
    nombre_producto = db.Column(db.String(30))
    marca = db.Column(db.String(30))
    nom_proveedor = db.Column(db.String(30))
    descripcion = db.Column(db.String(100))
    precio = db.Column(db.Integer)   
    foto = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
           
    def serialize(self):
        return {
            "id_producto": self.id_producto,
            "sku": self.sku,
            "nombre_producto": self.nombre_producto,
            "marca": self.marca,
            "nom_proveedor": self.nom_proveedor,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "foto": self.foto,
            "cantidad": self.cantidad
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla info_pago para almacenar los datos de pago de los usuarios
class info_pago (db.Model):
    __tablename__ = 'info_pago'
    correlativo = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(30))
    medio_pago = db.Column(db.String(20))
    cuotas = db.Column(db.Integer)
    
    def serialize(self):
        return {
            "correlativo": self.correlativo,
            "tipo_documento": self.tipo_documento,
            "medio_pago": self.medio_pago,
            "cuotas": self.cuotas,
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creación de tabla Mis_compras para almacenar los productos comprados por los usuarios
class mis_compras (db.Model):
    __tablename__ = 'mis_compras'
    id = db.Column(db.Integer, primary_key=True)
    id_compra = db.Column(db.Integer, ForeignKey('compra.id_comp'))
    FK_compra_id_compra = relationship('compra')
    id_producto = db.Column(db.Integer)
    #FK_compras_compra = relationship('compra')
    rut = db.Column(db.Integer) #, ForeignKey('compra.rut'))
    #FK_compras_usercompra = relationship('compra')
    correlativo = db.Column(db.Integer) #, ForeignKey('info_pago.correlativo'))    
    #FK_compras_infopago = relationship('info_pago')
    
    def serialize(self):
        return {
            "id_compra": self.id_compra,
            "id_producto": self.id_producto,
            "rut": self.rut,
            "correlativo": self.correlativo,
                        
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla Region para almacenar las regiones de Chile
class region (db.Model):
    __tablename__ = 'region'
    id_region = db.Column(db.Integer, primary_key=True)
    nom_region = db.Column(db.String(50))
    
    def serialize(self):
        return {
            "id_region": self.id_region,
            "nom_region": self.nom_region,
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla provincia
class provincia (db.Model):
    __tablename__ = 'provincia'
    id_provincia = db.Column(db.Integer, primary_key=True)
    nom_provincia = db.Column(db.String(50))
    id_region = db.Column(db.Integer, ForeignKey('region.id_region'))
    FK_provincia_region = relationship('region')
    
    def serialize(self):
        return {
            "id_provincia": self.id_provincia,
            "nom_provincia": self.nom_provincia,
            "id_region": self.id_region,
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla comuna
class comuna (db.Model):
    __tablename__ = 'comuna'
    id_comuna = db.Column(db.Integer, primary_key=True)
    nom_comuna = db.Column(db.String(50))
    id_provincia = db.Column(db.Integer, ForeignKey('provincia.id_provincia'))
    FK_comuna_provincia = relationship('provincia')
    #id_region = db.Column(db.Integer, ForeignKey('provincia.id_region'))
    #FK_comuna_provincia_region = relationship('provincia')
    
    
    def serialize(self):
        return {
            "id_comuna": self.id_comuna,
            "nom_comuna": self.nom_comuna,
            "id_provincia": self.id_provincia
            #"id_region": self.id_region,
            
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla direcciones
class direcciones (db.Model):
    __tablename__ = 'direcciones'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, ForeignKey('cliente.rut'))
    FK_direcciones_cliente = relationship('cliente')
    id_comuna = db.Column(db.Integer, ForeignKey('comuna.id_comuna'))
    FK_direcciones_comuna = relationship('comuna')
    id_provincia = db.Column(db.Integer)#, ForeignKey('comuna.id_provincia'))
    #FK_direcciones_provincia = relationship('comuna')
    #id_region = db.Column(db.Integer, ForeignKey('comuna.id_region'))
    #FK_direcciones_region = relationship('comuna')
    id_ubicacion = db.Column(db.Integer, ForeignKey('ubicacion.id_ubicacion'))
    FK_direcciones_ubicacion = relationship('ubicacion')
    
    def serialize(self):
        return {
            "rut": self.rut,
            "id_comuna": self.id_comuna,
            "id_provincia": self.id_provincia,
            #"id_region": self.id_region,
            "id_ubicacion": self.id_ubicacion
        }    
            
    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
#Creación de tabla de Cliente.
class cliente (db.Model):
    rut = db.Column(db.Integer, primary_key=True)
    dv = db.Column(db.String(1))
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    codigo_postal = db.Column(db.Integer)
    nacionalidad = db.Column(db.String(30))
    pasaporte = db.Column(db.String(12))
    user = db.Column(db.String(30), ForeignKey('usuario.user'))
    password = db.Column(db.String(10), ForeignKey('usuario.password'))
    calle = db.Column(db.String(50))
    numero = db.Column(db.Integer)
    
    def serializer (self):
        return {
            "rut": self.rut,
            "dv": self.dv,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "telefono": self.telefono,
            "sexo": self.sexo,
            "codigo_postal": self.codigo_postal,
            "nacionalidad": self.nacionalidad,
            "pasaporte": self.pasaporte,
            "user": self.user,
            "password": self.password,
            "calle": self.calle,
            "numero": self.numero,
        }                   

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
#Creación de tabla de compras.
class compra (db.Model):
    __tablename__ = 'compra'
    id_comp = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, ForeignKey('cliente.rut'))
    FK_cliente_compra = relationship('cliente')
    id_prod = db.Column(db.Integer, ForeignKey('producto.id_producto'))
    FK_compra_producto = relationship('producto')
    fecha_compra = db.Column(db.Date)
    fecha_entrega = db.Column(db.Date)
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    foto_producto = db.Column(db.String(100))
    nombre_producto = db.Column(db.String(30))
    valor_envio = db.Column(db.Integer)
    
    def serializer (self):
        return {
            "id_comp": self.id_comp,
            "rut": self.rut,
            "id_prod": self.id_prod,
            "fecha_compra": self.fecha_compra,
            "fecha_entrega": self.fecha_entrega,
            "cantidad": self.cantidad,
            "precio": self.precio,
            "foto_producto": self.foto_producto,
            "nombre_producto": self.nombre_producto,
            "valor_envio": self.valor_envio,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    