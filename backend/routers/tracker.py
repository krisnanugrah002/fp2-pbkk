from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import crud
import schemas
import models
from database import get_db
from routers.auth import get_current_user

router = APIRouter()

@router.get("/weight", response_model=List[schemas.WeightLogResponse])
def read_weight_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_weight_logs(db, user_id=current_user.id, skip=skip, limit=limit)

@router.post("/weight", response_model=schemas.WeightLogResponse)
def create_weight_log(log: schemas.WeightLogCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_weight_log(db=db, log=log, user_id=current_user.id)

@router.get("/food", response_model=List[schemas.FoodLogResponse])
def read_food_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_food_logs(db, user_id=current_user.id, skip=skip, limit=limit)

@router.post("/food", response_model=schemas.FoodLogResponse)
def create_food_log(log: schemas.FoodLogCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_food_log(db=db, log=log, user_id=current_user.id)

@router.get("/activity", response_model=List[schemas.ActivityLogResponse])
def read_activity_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_activity_logs(db, user_id=current_user.id, skip=skip, limit=limit)

@router.post("/activity", response_model=schemas.ActivityLogResponse)
def create_activity_log(log: schemas.ActivityLogCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_activity_log(db=db, log=log, user_id=current_user.id)