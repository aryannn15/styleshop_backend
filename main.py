import os
from fastapi import FastAPI
from pydantic import BaseModel
from recommendations import get_recommendations
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# CORS (safe for demo — tighten later in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def root():
    return {"status": "Backend is running"}

class UserInput(BaseModel):
    gender: str
    body_shape: str
    occasion: str
    skin_tone: str

@app.post("/recommend")
def recommend(user: UserInput):
    return get_recommendations(user.dict())

# -------- TEST SUPABASE CONNECTION --------
@app.get("/test-db")
def test_db():
    response = supabase.table("coupons").select("*").limit(1).execute()
    return response.data