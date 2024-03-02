from fastapi import FastAPI, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from database import SessionLocal, Base
from models import User, UserIn, UserOut, WallCreate, WallOut, MessageCreate, MessageOut
from pydantic import ValidationError
from passlib.context import CryptContext

app = FastAPI()

# Dependency for getting database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User endpoints

@app.post("/users/", response_model=UserOut)
async def create_user(user_in: UserIn, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user_in.password)
    user = User(login=user_in.login, password=hashed_password)
    db.add(user)
    db.commit()
    return UserOut.from_orm(user)

@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut.from_orm(user)

# Wall endpoints

@app.post("/walls/", response_model=WallOut)
async def create_wall(wall_create: WallCreate, db: Session = Depends(get_db)):
    wall = Wall(content=wall_create.content, user_id=wall_create.user_id)
    db.add(wall)
    db.commit()
    return WallOut.from_orm
