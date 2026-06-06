from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class BMIInput(BaseModel):
    weight_kg: float
    height_cm: float

class TDEEInput(BaseModel):
    weight_kg: float
    height_cm: float
    age: int
    gender: str
    activity_level: str

@router.post("/bmi")
def calculate_bmi(data: BMIInput):
    height_m = data.height_cm / 100
    bmi = data.weight_kg / (height_m ** 2)
    category = "Ideal"
    if bmi < 18.5:
        category = "Underweight"
    elif bmi > 25:
        category = "Overweight"
    return {"bmi": round(bmi, 2), "category": category}

@router.post("/tdee")
def calculate_tdee(data: TDEEInput):
    if data.gender.lower() == "male":
        bmr = 88.362 + (13.397 * data.weight_kg) + (4.799 * data.height_cm) - (5.677 * data.age)
    else:
        bmr = 447.593 + (9.247 * data.weight_kg) + (3.098 * data.height_cm) - (4.330 * data.age)
    
    multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }
    multiplier = multipliers.get(data.activity_level.lower(), 1.2)
    tdee = bmr * multiplier
    return {"tdee": round(tdee, 2), "bmr": round(bmr, 2)}