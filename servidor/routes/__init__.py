from flask import current_app,request,render_template,redirect,url_for
from servidor.database.item import Item
from servidor.utils import capture_form,Message
from tortoise.exceptions import IntegrityError
import contextlib
app = current_app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/item')
async def item():
    itens = await Item.all()
    return render_template('item.html',itens=itens,campos=['Id','Codigo','Nome','Valor'],enumerate=enumerate)

@app.route('/item/add',methods=['GET','POST'])
async def item_add():
    if request.method == 'GET':
        return render_template('item_add.html')
    elif request.method == 'POST':
        mapa = {'codigo':'strip','nome':'strip','valor':'float'}
        data = await capture_form(request.form,mapa)
        for key in mapa:
            if data.get(key) == None:
                return render_template('item_add.html',**Message.item_value_nao_informado(key),ram=data)
        try:
            item = await Item.create(**data)
            await item.save()
            return render_template('item_add.html',**Message.item_adicionado(data['nome']))
        except IntegrityError as error:
            error = str(error)
            error = error[error.rfind('.')+1:]
            return render_template('item_add.html',**Message.item_ja_existe(data[error]),ram=data)

@app.route('/item/update',methods=['GET','POST'])
async def item_update():
    if request.method == 'GET':
        Id = request.args.get('Id')

        if Id and Id.isnumeric():
            item = await Item.filter(id=int(Id)).first()
            if item:
                return render_template('item_update.html',item=item, message=request.args.get('message'),color_message=request.args.get('color_message'))
    else:
        mapa = {'id':'int','codigo':'strip','nome':'strip','valor':'float'}
        data = await capture_form(request.form,mapa)
        for key in mapa:
            if data.get(key) == None:
                with contextlib.suppress():
                    return redirect(url_for('item_update',Id=data.get('id'),**Message.item_value_nao_informado(key)))   
        try:
            await Item.filter(id=data.get('id')).update(codigo = data.get('codigo'), nome = data.get('nome'), valor = data.get('valor'))
        except IntegrityError as error:
            error = str(error)
            error = error[error.rfind('.')+1:]
            with contextlib.suppress():
                return redirect(url_for('item_update',Id=data.get('id'),**Message.item_ja_existe(data[error])))
    return redirect(url_for('item'))

@app.route('/item/delete')
async def item_delete():
    Id = request.args.get('Id')
    if Id and Id.isnumeric():
        with contextlib.suppress():
            await Item.filter(id=int(Id)).delete()
    return redirect(url_for('item'))
