from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db, URLModel
from db.schemas import URLCreate, URLStats
from router.shortener_router import app as shortener_router
from utils.exceptionHandler import custom_http_exception_handler

app = FastAPI(title="Simplified URL Shortener")

app.exception_handler(custom_http_exception_handler)
app.include_router(shortener_router)
