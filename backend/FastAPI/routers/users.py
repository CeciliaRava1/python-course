### main ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# User entity
# Basemodel allows to create an entity
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# In 'DataBase'
users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
              User(id=3, name="Haakon", surname="Dahlberg", url="https://haakon.com", age=33)]


# Get - - - 
@router.get('/usersjson')
async def usersjson():
    return [{"name":"Brais", "surname":"Moure", "url":"https://moure.dev", "age": 35},
            {"name":"Moure", "surname":"Dev", "url":"https://mouredev.com", "age": 35},
            {"name":"Haakon", "surname":"Dahlberg", "url":"https://Haakon.com", "age": 33}]

@router.get('/users')
async def users():
    return users_list

# Path
@router.get('/user/{id}')
async def user(id: int):
    return search_user(id)

# Query
@router.get('/user/')
async def user(id: int):
    return search_user(id)


# Post - - - 
@router.post('/user/', response_model=user, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="user does exists")
    else:
        users_list.append(user)
        return user

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"user not found"}
    

# Put - - - 
@router.put('/user/')
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":"user not updated"}
    else:
        return user


# Delete - - - 
@router.delete('/user/{id}')
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error":"user not deleted"}
    
    


