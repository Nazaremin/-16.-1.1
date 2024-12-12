from typing import Annotated
from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Главная страница</h1>"

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[
        int,
        Path(title="Enter User ID", ge=1, le=100, example=1)
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=24)
    ]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
