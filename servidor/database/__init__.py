from tortoise import Tortoise
from servidor.database.item import Item
async def app_init():
    await Tortoise.init(
        db_url='sqlite://storage.db',
        modules={'Model':['servidor.database']}
    )
    await Tortoise.generate_schemas()