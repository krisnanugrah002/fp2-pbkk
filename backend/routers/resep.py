from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import crud
import schemas
import models
from database import get_db
from routers.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.RecipeResponse])
def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes

@router.post("/", response_model=schemas.RecipeResponse)
def create_recipe(
    recipe: schemas.RecipeCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_recipe(db=db, recipe=recipe, user_id=current_user.id)