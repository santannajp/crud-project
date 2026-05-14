from fastapi import fastAPI
from database import engine
import models
from router import router

models.Base.metadata.create_all(bind=engine)

app = fastAPI()
app.include_router(router)

