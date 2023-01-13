from fastapi import FastAPI, Request, HTTPException
from database import User
from database import database as connection
from schemas import UserRequestModel
from schemas import UserResponseModel

app = FastAPI(title='Proyecto framework FLP',
            description='Testing web page')

@app.on_event('startup')
def starup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.post("/users")
async def create_user(user_request: UserRequestModel):
    user =User.create(
        username=user_request.username,
        email=user_request.email,
        password=user_request.password)
    return user_request

@app.get('/user/{user_id}') 
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()   

    if user:
        return UserResponseModel(id=user.id,
                                username=user.username,
                                email=user.email,
                                password=user.password)
    else:
        return HTTPException(404, 'User not found')

#@app.put("/about")
#def about():
#    return {"Data": "Acerca"}

#@app.delete("/about")
#def about():
#    return {"Data": "Acerca"}
