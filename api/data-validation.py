from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr,HttpUrl
from datetime  import date
import uvicorn
from uuid import UUID, uuid4

# =========================================================
# FastAPI application
# =========================================================
app = FastAPI(
    title="Data Validation API",
    description="An API for validating data using Pydantic models.",
    version="1.0.0",
)

# =========================================================
# root endpoint
# =========================================================
@app.get("/")
async def root():
    return {"message": "Welcome to the Data Validation API!"}

# =========================================================
# Data model for validation
# =========================================================
class Product_Details(BaseModel):
    id: int = Field(gt=50)
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(default=None, max_length=200)
    price: float = Field(gt=0)
    product_url: HttpUrl


# =========================================================
# User details model for validation
# =========================================================
class UserDetails(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(lt=100,gt=18)
    aadhar_id: str = Field(pattern=r"^\d{12}$")
    date_of_birth: date
    phone_number: int = Field(eq=10)
# =========================================
# Get Product Details
# ==========================================
@app.get("/product_details",response_model=Product_Details)
def product():

    return Product_Details(
        id=51,
        name="Laptop",
        description="A sample product",
        price=75000.0,
        product_url = "https://testing.com/"
    )
# =======================================================
# user details
# =======================================================
@app.get("/user_details",response_model=UserDetails)

def user_details():

    return UserDetails(
        username="santhi-bhogavalli",
        email="santhi.bhogavalli@hotmail.com",
        age=32,
        aadhar_id="123445676789",
        date_of_birth="1999-09-20",
        phone_number=1234567898
    )

# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    uvicorn.run(
        "data-validation:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
    )