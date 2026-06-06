from sqlalchemy.orm import Session
import models
import schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        age=user.age,
        gender=user.gender,
        height_cm=user.height_cm,
        activity_level=user.activity_level
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def create_recipe(db: Session, recipe: schemas.RecipeCreate, user_id: int = None):
    db_recipe = models.Recipe(**recipe.model_dump(), created_by=user_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_weight_logs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.WeightLog).filter(models.WeightLog.user_id == user_id).offset(skip).limit(limit).all()

def create_weight_log(db: Session, log: schemas.WeightLogCreate, user_id: int):
    db_log = models.WeightLog(**log.model_dump(), user_id=user_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_food_logs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.FoodLog).filter(models.FoodLog.user_id == user_id).offset(skip).limit(limit).all()

def create_food_log(db: Session, log: schemas.FoodLogCreate, user_id: int):
    db_log = models.FoodLog(**log.model_dump(), user_id=user_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_activity_logs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.ActivityLog).filter(models.ActivityLog.user_id == user_id).offset(skip).limit(limit).all()

def create_activity_log(db: Session, log: schemas.ActivityLogCreate, user_id: int):
    db_log = models.ActivityLog(**log.model_dump(), user_id=user_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log