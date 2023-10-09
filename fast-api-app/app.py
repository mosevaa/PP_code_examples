from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:63342",
    "http://127.0.0.1",
    "http://127.0.0.1:63342"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', response_model=UserInfo)
async def root():
    return {'data': 'Hello World!'}


@app.get('/data', response_model=UserInfo)
async def root():
    user = UserInfo(
        name='Jonh',
        surname='Jack',
        age=21
    )
    return user
