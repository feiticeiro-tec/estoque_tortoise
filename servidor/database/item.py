from tortoise.models import Model
from tortoise import fields
from tortoise.exceptions import IntegrityError
class Item(Model):
    id = fields.IntField(pk=True)
    codigo = fields.CharField(50,unique=True)
    nome = fields.TextField()
    valor = fields.FloatField()
    data_criado = fields.DatetimeField(auto_now=True)
    data_update = fields.DatetimeField(auto_now=True)
    def get(self,key):
        if key:
            key = key.lower()
            if key == 'id':
                return self.id
            elif key == 'codigo':
                return self.codigo
            elif key == 'nome':
                return self.nome
            elif key == 'valor':
                return self.valor
            elif key == 'data_criado':
                return self.data_criado
            elif key == 'data_update':
                return self.data_update