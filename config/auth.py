from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from fastapi import Depends, HTTPException, APIRouter
from config.db import db_dependency
from models.staff import Staff
from fastapi.security import OAuth2PasswordBearer
login_router = APIRouter()


# Secret key — generate with: openssl rand -hex 32
SECRET_KEY = "supersecretkey1234567890"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


@login_router.post("/login" ,tags=["login"])
async def login(db: db_dependency, email: str):
    staff = db.query(Staff).filter(Staff.email == email).first()
    if not staff:
        raise HTTPException(status_code=401, detail="Invalid email")

    # Create JWT
    token_data = {"sub": staff.email, "user_type": staff.department}
    access_token = create_access_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    email = payload.get("sub")
    user_type = payload.get("user_type")

    if not email or not user_type:
        raise HTTPException(status_code=401, detail="Invalid token data")

    return {"email": email, "user_type": user_type}
