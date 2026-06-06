from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class UserBase(BaseModel):
    username: str
    email: EmailStr
    age: int
    gender: str
    height_cm: float
    activity_level: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class RecipeBase(BaseModel):
    title: str
    description: str
    ingredients: str
    instructions: str
    calories: float

class RecipeCreate(RecipeBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Healthy Salt Bread",
                "description": "Roti garam sehat dengan kalori terkontrol",
                "ingredients": "Tepung, air, ragi, garam laut, mentega tanpa garam",
                "instructions": "Campur bahan kering, masukkan air, uleni hingga kalis, tambahkan mentega, panggang.",
                "calories": 250.0
            }
        }
    }

class RecipeResponse(RecipeBase):
    id: int
    created_by: Optional[int] = None

    class Config:
        from_attributes = True

class WeightLogBase(BaseModel):
    weight_kg: float

class WeightLogCreate(WeightLogBase):
    pass

class WeightLogResponse(WeightLogBase):
    id: int
    user_id: int
    log_date: date

    class Config:
        from_attributes = True

class FoodLogBase(BaseModel):
    food_name: str
    calories: float
    protein_g: float

class FoodLogCreate(FoodLogBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "food_name": "Sweetofdough Soft Cookies",
                "calories": 210.5,
                "protein_g": 3.0
            }
        }
    }

class FoodLogResponse(FoodLogBase):
    id: int
    user_id: int
    log_date: date

    class Config:
        from_attributes = True

class ActivityLogBase(BaseModel):
    activity_name: str
    calories_burned: float

class ActivityLogCreate(ActivityLogBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "activity_name": "Fast Walking 5.25 km",
                "calories_burned": 320.0
            }
        }
    }

class ActivityLogResponse(ActivityLogBase):
    id: int
    user_id: int
    log_date: date

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None