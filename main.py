from fastapi import FastAPI
from pydantic import BaseModel
from recommendations import get_recommendations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (safe for demo — tighten later in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route (important for testing Render deployment)
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