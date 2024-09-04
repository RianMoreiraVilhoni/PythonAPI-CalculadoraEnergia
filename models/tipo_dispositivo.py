from peewee import AutoField, CharField, FloatField, Model

from config.database import database

class TipoDispositivoDB(Model):
    id = AutoField(column_name='tipo_dispositivo_id')
    nome = CharField(column_name='tipo_dispositivo_nome')

    class Meta:
        database = database
        table_name = 'tipo_dispositivo'