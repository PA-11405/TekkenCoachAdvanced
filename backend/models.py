from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Move(Base):
    __tablename__ = "moves"
    id = Column(Integer, primary_key=True, index=True)
    move_name = Column(String, unique=True, index=True)
    character = Column(String, index=True)
    frame_data = Column(JSON)       # e.g., {"startup": 16, "block": -2, "hit": 6, "counter_hit": "knockdown"}
    common_issues = Column(JSON)      # list of strings
    best_counters = Column(JSON)      # list of dicts: [{"character": "Leroy", "counter": "b+1 parry"}, ...]
    in_depth_counterplay = Column(String)
    image_url = Column(String)        # URL for character image
