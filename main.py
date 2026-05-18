from fastapi import FastAPI,status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import models
from database import engine
from routers import auth,jobing,admin,user

app= FastAPI()
models.base.metadata.create_all(bind=engine)

app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
async def read_root():
    return FileResponse("frontend/index.html")

@app.get("/healthy",status_code=status.HTTP_200_OK)
def read_main():
    return {"status":"healthy"}

app.include_router(auth.router)
app.include_router(jobing.routerJobs)
app.include_router(admin.router)
app.include_router(user.router)