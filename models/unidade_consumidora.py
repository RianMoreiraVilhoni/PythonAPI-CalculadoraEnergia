from peewee import AutoField, CharField, FloatField, Model, ForeignKeyField

from config.database import database
from models.tipo_consumidor import TipoConsumidorDB

class UnidadeConsumidoraDB(Model):
    id = AutoField(column_name='unidade_consumidora_id')
    nombre = CharField(column_name='unidade_consumidor_nome')
    tipo = ForeignKeyField(
        column_name='unidade_consumidor_tipo_id',
        model=TipoConsumidorDB,
        backref='unidade_consumidora',
    )

    class Meta:
        database = database
        table_name = 'unidade_consumidora'