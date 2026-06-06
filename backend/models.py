from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import date
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    age = Column(Integer)
    gender = Column(String)
    height_cm = Column(Float)
    activity_level = Column(String)

    weight_logs = relationship("WeightLog", back_populates="owner", cascade="all, delete-orphan")
    food_logs = relationship("FoodLog", back_populates="owner", cascade="all, delete-orphan")
    activity_logs = relationship("ActivityLog", back_populates="owner", cascade="all, delete-orphan")
    recipes = relationship("Recipe", back_populates="creator")

class WeightLog(Base):
    __tablename__ = "weight_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    weight_kg = Column(Float)
    log_date = Column(Date, default=date.today)

    owner = relationship("User", back_populates="weight_logs")

class FoodLog(Base):
    __tablename__ = "food_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    food_name = Column(String)
    calories = Column(Float)
    protein_g = Column(Float)
    log_date = Column(Date, default=date.today)

    owner = relationship("User", back_populates="food_logs")

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    activity_name = Column(String)
    calories_burned = Column(Float)
    log_date = Column(Date, default=date.today)

    owner = relationship("User", back_populates="activity_logs")

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    ingredients = Column(Text)
    instructions = Column(Text)
    calories = Column(Float)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    creator = relationship("User", back_populates="recipes")