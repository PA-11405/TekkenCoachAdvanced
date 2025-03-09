Tekken Coach Advanced 

A smart, AI-powered assistant designed to help Tekken 8 players understand, counter, and improve against specific character moves. This full-stack project combines FastAPI, React, and scraping tools to provide matchup insights and visual references.

- Move Analyzer: Lookup difficult moves (e.g., Jin's d2, Law's 1,1,1) with detailed counterplay.
- Character Visuals: Automatically displays images of each character next to their move breakdown.
- Live Data Integration: Scrapes or imports real data (like frame info and properties) from sources like RBNorway.
- Full-Stack: 
  - Backend: Python 3, FastAPI
  - Frontend: React, Material UI (with dark theme)
  - Database Ready: Easily expandable to support more characters/moves
- Error Handling: Backend scripts gracefully manage data fetching errors and invalid requests.

Getting Started

Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
