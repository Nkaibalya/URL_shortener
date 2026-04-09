from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db, URLModel
from db.schemas import URLCreate, URLStats
from fastapi.responses import RedirectResponse
from utils.exceptionHandler import custom_http_exception_handler
import string



def encode_base62(n: int) -> str:
    chars = string.digits + string.ascii_letters
    return encode_base62(n // 62) + chars[n % 62] if n > 0 else (chars[0] if n == 0 else "")

def health_check():
    return {"status": "ok", "message": "URL Shortener is running", "version": "1.0.0"}

def shorten_url(data: URLCreate, db: Session = Depends(get_db)):
    target_url = str(data.url).rstrip('/')#--for normalize url
    
    existing_url = db.query(URLModel).filter(URLModel.original_url == target_url).first()
    
    if existing_url:
        return {
            "short_url": f"/{existing_url.short_code}", 
            "code": existing_url.short_code, 
            "status": "existing"
        }

    new_url = URLModel(original_url=target_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    
    new_url.short_code = encode_base62(new_url.id)
    db.commit()
    
    return {
        "short_url": f"/{new_url.short_code}", 
        "code": new_url.short_code, 
        "status": "new"
    }

def redirect_to_long_url(short_code: str, db: Session = Depends(get_db)):
    url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    url_record.clicks += 1
    db.commit()
    return RedirectResponse(url=url_record.original_url)

def get_url_stats(short_code: str, db: Session = Depends(get_db)):
    url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_record   