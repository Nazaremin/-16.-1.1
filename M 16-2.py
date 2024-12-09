from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from fastapi import Query
from typing import Annotated

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Главная страница</h1>"

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID")]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Query(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Query(ge=18, le=120, description="Enter age")]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
