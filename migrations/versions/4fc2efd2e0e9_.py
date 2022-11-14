"""empty message

Revision ID: 4fc2efd2e0e9
Revises: 
Create Date: 2022-10-16 18:14:31.509195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fc2efd2e0e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info_pago',
    sa.Column('correlativo', sa.Integer(), nullable=False),
    sa.Column('tipo_documento', sa.String(length=30), nullable=True),
    sa.Column('medio_pago', sa.String(length=20), nullable=True),
    sa.Column('cuotas', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('correlativo')
    )
    op.create_table('producto',
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=10), nullable=True),
    sa.Column('nombre_producto', sa.String(length=30), nullable=True),
    sa.Column('marca', sa.String(length=30), nullable=True),
    sa.Column('nom_proveedor', sa.String(length=30), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('foto', sa.String(length=100), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_producto')
    )
    op.create_table('region',
    sa.Column('id_region', sa.Integer(), nullable=False),
    sa.Column('nom_region', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id_region')
    )
    op.create_table('ubicacion',
    sa.Column('id_ubicacion', sa.Integer(), nullable=False),
    sa.Column('latitud', sa.Integer(), nullable=True),
    sa.Column('longitud', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_ubicacion')
    )
    op.create_table('usuario',
    sa.Column('user', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('user', 'password')
    )
    op.create_table('categorias',
    sa.Column('id_categoria', sa.Integer(), nullable=False),
    sa.Column('desc_categoria', sa.String(length=30), nullable=True),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_producto'], ['producto.id_producto'], ),
    sa.PrimaryKeyConstraint('id_categoria')
    )
    op.create_table('cliente',
    sa.Column('rut', sa.Integer(), nullable=False),
    sa.Column('dv', sa.String(length=1), nullable=True),
    sa.Column('nombres', sa.String(length=50), nullable=True),
    sa.Column('apellidos', sa.String(length=50), nullable=True),
    sa.Column('telefono', sa.Integer(), nullable=True),
    sa.Column('sexo', sa.String(length=1), nullable=True),
    sa.Column('codigo_postal', sa.Integer(), nullable=True),
    sa.Column('nacionalidad', sa.String(length=30), nullable=True),
    sa.Column('pasaporte', sa.String(length=12), nullable=True),
    sa.Column('user', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=10), nullable=True),
    sa.Column('calle', sa.String(length=50), nullable=True),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['password'], ['usuario.password'], ),
    sa.ForeignKeyConstraint(['user'], ['usuario.user'], ),
    sa.PrimaryKeyConstraint('rut')
    )
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_producto'], ['producto.id_producto'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('provincia',
    sa.Column('id_provincia', sa.Integer(), nullable=False),
    sa.Column('nom_provincia', sa.String(length=50), nullable=True),
    sa.Column('id_region', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_region'], ['region.id_region'], ),
    sa.PrimaryKeyConstraint('id_provincia')
    )
    op.create_table('compra',
    sa.Column('id_comp', sa.Integer(), nullable=False),
    sa.Column('rut', sa.Integer(), nullable=True),
    sa.Column('id_prod', sa.Integer(), nullable=True),
    sa.Column('fecha_compra', sa.Date(), nullable=True),
    sa.Column('fecha_entrega', sa.Date(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('foto_producto', sa.String(length=100), nullable=True),
    sa.Column('nombre_producto', sa.String(length=30), nullable=True),
    sa.Column('valor_envio', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_prod'], ['producto.id_producto'], ),
    sa.ForeignKeyConstraint(['rut'], ['cliente.rut'], ),
    sa.PrimaryKeyConstraint('id_comp')
    )
    op.create_table('comuna',
    sa.Column('id_comuna', sa.Integer(), nullable=False),
    sa.Column('nom_comuna', sa.String(length=50), nullable=True),
    sa.Column('id_provincia', sa.Integer(), nullable=True),
    sa.Column('id_region', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_provincia'], ['provincia.id_provincia'], ),
    sa.ForeignKeyConstraint(['id_region'], ['provincia.id_region'], ),
    sa.PrimaryKeyConstraint('id_comuna')
    )
    op.create_table('direcciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rut', sa.Integer(), nullable=True),
    sa.Column('id_comuna', sa.Integer(), nullable=True),
    sa.Column('id_provincia', sa.Integer(), nullable=True),
    sa.Column('id_region', sa.Integer(), nullable=True),
    sa.Column('id_ubicacion', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_comuna'], ['comuna.id_comuna'], ),
    sa.ForeignKeyConstraint(['id_provincia'], ['comuna.id_provincia'], ),
    sa.ForeignKeyConstraint(['id_region'], ['comuna.id_region'], ),
    sa.ForeignKeyConstraint(['id_ubicacion'], ['ubicacion.id_ubicacion'], ),
    sa.ForeignKeyConstraint(['rut'], ['cliente.rut'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mis_compras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_compra', sa.Integer(), nullable=True),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.Column('rut', sa.Integer(), nullable=True),
    sa.Column('correlativo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['correlativo'], ['info_pago.correlativo'], ),
    sa.ForeignKeyConstraint(['id_compra'], ['compra.id_comp'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['compra.id_prod'], ),
    sa.ForeignKeyConstraint(['rut'], ['compra.rut'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mis_compras')
    op.drop_table('direcciones')
    op.drop_table('comuna')
    op.drop_table('compra')
    op.drop_table('provincia')
    op.drop_table('favoritos')
    op.drop_table('cliente')
    op.drop_table('categorias')
    op.drop_table('usuario')
    op.drop_table('ubicacion')
    op.drop_table('region')
    op.drop_table('producto')
    op.drop_table('info_pago')
    # ### end Alembic commands ###