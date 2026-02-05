# CRUD: create, read, update, delete
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.item_schema import ItemSchema
from app.services.crud_services import create_item, get_item, update_item, delete_item, list_items
from app.utils.exception import ItemNotFoundError
from app.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/items", tags=["Items"])

# POST local host:8000/items
@router.post("/", response_model=ItemSchema)
def create_new_item(item: ItemSchema, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    return create_item(item, db)

@router.get("/{item_id}", response_model=ItemSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get an item by its ID.
    """
    try:
        return get_item(item_id, db)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    
@router.put("/{item_id}", response_model=ItemSchema)
def update_existing_item(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    """
    Update an existing item by its ID.
    """
    try:
        return update_item(item_id, item, db)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    
@router.delete("/{item_id}")
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.
    """
    try:
        return delete_item(item_id, db)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    
@router.get("/", response_model=list[ItemSchema])
def list_all_items(db: Session = Depends(get_db)):
    """
    List all items.
    """
    return list_items(db)