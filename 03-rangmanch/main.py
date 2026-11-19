from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from routes.reviews import router as reviews_router



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

app.include_router(reviews_router)

@app.get("/")
def root():
   return {"message":"Welcome to rangmanch review API"}