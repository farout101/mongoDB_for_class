from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import lsist_serial
from bson import ObjectId   

router = APIRouter()

# Get Request method
@router.get("/")
async def get_todos():
    todos = lsist_serial(collection_name.find())
    return todos

# Post Request method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return lsist_serial(collection_name.find())