from fastapi import FastAPI
from routers.task import router as task_router
from routers.users import router as user_router


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user_router)
app.include_router(task_router)