from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.polo import router as PoloAPIRouter

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methos=["*"],
    allow_headers=["*"],
)

app.include_router(PoloAPIRouter, tags=["polo"], prefix="/polo")

@app.get("/", tags=["home"])
def read_root():
    return {'message':'Welcome to this app'}
