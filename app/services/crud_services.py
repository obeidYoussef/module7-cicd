from app.schemas.item_schema import ItemSchema
from app.utils.exception import ItemNotFoundError
from app.models.item_model import Item
from sqlalchemy.orm import Session

"""
input: 1, "Item1", 10.5
db[1]: Item(id=1, name="Item1", value=10.5)
db[2]: Item(id=2, name="Item2", value=20.0)

"""

# db: dict[int, Item] = {}

# def create_item(item: Item):
#     db[item.id] = item
#     return item

def create_item(item: ItemSchema, db: Session):
    db_item = Item(name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# def get_item(item_id: int):
#     if item_id not in db:
#         raise ItemNotFoundError(item_id)
#     return db[item_id]

def get_item(item_id: int, db: Session) -> ItemSchema:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise ItemNotFoundError(item_id)
    return db_item

# def update_item(item_id: int, item: Item):
#     if item_id not in db:
#         raise ItemNotFoundError(item_id)
#     db[item_id] = item
#     return item

def update_item(item_id: int, item: ItemSchema, db: Session) -> ItemSchema:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise ItemNotFoundError(item_id)
    db_item.name = item.name
    db_item.value = item.value
    db.commit()
    db.refresh(db_item)
    return db_item

# def delete_item(item_id: int):
#     if item_id not in db:
#         raise ItemNotFoundError(item_id)
#     db.pop(item_id)
#     return {"message": f"Item with id {item_id} deleted."}

def delete_item(item_id: int, db: Session):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise ItemNotFoundError(item_id)
    db.delete(db_item)
    db.commit()
    return {"message": f"Item with id {item_id} deleted."}

# def list_items():
#     return list(db.values())

def list_items(db: Session):
    all_items = db.query(Item).all()
    return all_items