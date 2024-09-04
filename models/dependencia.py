from peewee import AutoField, CharField, FloatField, Model, ForeignKeyField

from config.database import database
from models.unidade_consumidora import UnidadeConsumidoraDB

class DependenciaDB(Model):
    id = AutoField(column_name='dependencia_id')
    nome = CharField(column_name='dependencia_nome')
    unidade_consumidora = ForeignKeyField(
        column_name='dependencia_unidade_consumidora',
        model=UnidadeConsumidoraDB,
        backref='dependencia',
    )

    class Meta:
        database = database
        db_table = 'dependencia'