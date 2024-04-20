import os
import uvicorn
from fastapi import FastAPI, status, Query, HTTPException, Form, Header , Body
import requests
import random
from reqest import auth
from sets import settings

#from keycloak import KeycloakOpenID

app = FastAPI()

@app.post('/auth')
def auth_user(username: str = Body(), password: str = Body()):
    user = auth(username=username, password=password)
    print(user)
    if (user.status_code != 200):
        raise HTTPException(401, 'bad user data')
    return user.json()['access_token']

@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {'message': 'service alive'}


@app.get("/get_random_movie")
async def get_random_movie():
    r_id = random.randint(298, 10000)
    r = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.2/films/{r_id}", headers={'X-API-KEY': '700211e1-f970-499f-9957-6bca24e2adb1'})
    return r.json()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))