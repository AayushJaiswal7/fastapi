from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables

@asynccontextmanager
async def lifespan(app:FastAPI):
   create_tables()
   print("Database tables created")
   yield
   print("Shutting down the app")
app=FastAPI(
   title="Rangmanch Review API",
   description="Theatre review API for Pune branch",
   lifespan=lifespan
)

@app.get("/")
def root():
   return {"message":"Welcom to rangmanch review API"}