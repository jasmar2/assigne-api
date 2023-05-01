from fastapi import APIRouter
from api.routers import project_router

api_router = APIRouter()

api_router.include_router(project_router.router, tags=["projects"])