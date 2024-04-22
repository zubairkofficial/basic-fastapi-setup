from fastapi import APIRouter
from appdatabase import Database
from models.Blog import Blog

router = APIRouter()

db = Database()

@router.get('/items')
async def all_items():
    relationships = [Blog.categories()]

    data = await db.with_relationships('blogs', relationships)

    return {"data" : data}

