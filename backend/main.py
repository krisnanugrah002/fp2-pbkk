from fastapi import FastAPI
from database import engine
import models
from routers import auth, kalkulator, resep, tracker

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitMate API")

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(kalkulator.router, prefix="/api/calculator", tags=["Calculators"])
app.include_router(resep.router, prefix="/api/recipes", tags=["Recipes"])
app.include_router(tracker.router, prefix="/api/tracker", tags=["Daily Tracker"])