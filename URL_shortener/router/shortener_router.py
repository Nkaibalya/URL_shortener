from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db, URLModel
from db.schemas import URLCreate, URLStats
from fastapi.responses import RedirectResponse
from service import shortener_services
app  = APIRouter()

@app.get("/health")
def health_check():
    return shortener_services.health_check()

@app.post("/shorten")
def shorten_url(data: URLCreate, db: Session = Depends(get_db)):
    return shortener_services.shorten_url(data, db)

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str, db: Session = Depends(get_db)):
    return shortener_services.redirect_to_long_url(short_code, db)

@app.get("/stats/{short_code}", response_model=URLStats)
def get_url_stats(short_code: str, db: Session = Depends(get_db)):
    return shortener_services.get_url_stats(short_code, db)