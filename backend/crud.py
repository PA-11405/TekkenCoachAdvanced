from sqlalchemy.orm import Session
from models import Move

def get_moves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Move).offset(skip).limit(limit).all()

def get_move_by_name(db: Session, move_name: str):
    return db.query(Move).filter(Move.move_name.ilike(f"%{move_name}%")).first()

def create_move(db: Session, move_data: dict):
    db_move = Move(**move_data)
    db.add(db_move)
    db.commit()
    db.refresh(db_move)
    return db_move
