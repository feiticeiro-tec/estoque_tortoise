class Message():
    @staticmethod
    def item_adicionado(nome):
        return {'message':f'Item {nome} Adicionado Com Sucesso!','color_message':'green'}
    
    @staticmethod
    def item_ja_existe(nome):
        return {'message':f'Item {nome} Já Existe!','color_message':'red'}
    
    @staticmethod
    def item_value_nao_informado(nome):
        return {'message':f'O Valor "{nome.title()}" Não Foi Informado!','color_message':'red'}