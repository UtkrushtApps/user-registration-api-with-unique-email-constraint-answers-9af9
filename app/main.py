from fastapi import FastAPI, HTTPException, Depends
from app.models import Base, User, UserCreate, UserOut
from app.database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=UserOut, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, full_name=user.full_name)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered.")
    return db_user

@app.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
