from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi import Path

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}
user_id_counter = 1

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

@app.get("/users")
def read_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=24)
    ]
):
    global user_id_counter
    user_id_counter += 1
    users[str(user_id_counter)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id_counter} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[
        int,
        Path(title="Enter User ID", example=1)
    ],
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=24)
    ]
):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[
        int,
        Path(title="Enter User ID", example=1)
    ]
):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[str(user_id)]
    return f"User {user_id} has been deleted"
