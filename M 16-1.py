
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Query

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Главная страница</h1>"

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
def read_user_info(username: str = Query(...), age: int = Query(...)):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
