from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn

from database import SessionLocal, engine, Base
from models import Move
import crud

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tekken Coach Advanced API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/moves")
def list_moves(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    moves = crud.get_moves(db, skip=skip, limit=limit)
    return {"moves": [move.move_name for move in moves]}

@app.get("/move/{move_name}")
def read_move(move_name: str, db: Session = Depends(get_db)):
    db_move = crud.get_move_by_name(db, move_name)
    if db_move is None:
        raise HTTPException(status_code=404, detail="Move not found")
    return db_move

# Populate the database with sample data if empty.
def init_db(db: Session):
    if db.query(Move).first() is None:
        sample_moves = [
            {
                "move_name": "Jin d+2",
                "character": "Jin",
                "frame_data": {"startup": 16, "block": -2, "hit": 6, "counter_hit": "knockdown"},
                "common_issues": ["Safe on block", "Fast startup", "Hard to punish"],
                "best_counters": [
                    {"character": "Leroy", "counter": "b+1 parry"},
                    {"character": "Steve", "counter": "duck and ws+1"}
                ],
                "in_depth_counterplay": "Backdash to avoid the move and punish the whiff with a fast jab or parry-based counter.",
                "image_url": "https://example.com/images/jin.png"
            },
            {
                "move_name": "Law 1,1,1",
                "character": "Law",
                "frame_data": {"startup": 12, "block": -3, "hit": 8, "counter_hit": "launcher"},
                "common_issues": ["Repeated safe attack", "Difficult to counter", "Predictable timing"],
                "best_counters": [
                    {"character": "Paul", "counter": "crouching block and punish"},
                    {"character": "Hwoarang", "counter": "forward dash and quick punishes"}
                ],
                "in_depth_counterplay": "Adopt a defensive stance with crouching block and counter-hit as soon as you detect the sequence.",
                "image_url": "https://example.com/images/law.png"
            }
        ]
        for move in sample_moves:
            crud.create_move(db, move)

@app.on_event("startup")
def startup_event():
    from database import SessionLocal
    db = SessionLocal()
    init_db(db)
    db.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
