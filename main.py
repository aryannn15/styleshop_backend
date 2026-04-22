import os
from fastapi import FastAPI
from pydantic import BaseModel
from recommendations import get_recommendations
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv

# NEW imports for coupon + QR
import secrets
import qrcode
import io
import base64


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


# -------- GENERATE COUPON + QR --------
@app.post("/generate-coupon")
def generate_coupon():

    # generate coupon code
    couponCode = "STYLE" + secrets.token_hex(3).upper()

    # insert into Supabase DB
    supabase.table("coupons").insert({
        "couponCode": couponCode,
        "discount": 10
    }).execute()

    # create QR code
    qr = qrcode.make(couponCode)

    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return {
        "couponCode": couponCode,
        "qr_image": qr_base64
    }

class CouponVerify(BaseModel):
    couponCode: str


@app.post("/verify-coupon")
def verify_coupon(data: CouponVerify):

    code = data.couponCode

    # find coupon in DB
    result = supabase.table("coupons").select("*").eq("couponCode", code).execute()

    if not result.data:
        return {"valid": False}

    coupon = result.data[0]

    if coupon["is_used"]:
        return {"valid": False, "message": "already used"}

    # mark coupon as used
    supabase.table("coupons").update({"is_used": True}).eq("couponCode", code).execute()

    return {
        "valid": True,
        "discount": coupon["discount"],
        "type": "percentage"

