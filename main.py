from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FeotusData(BaseModel):
    baselineValue: float
    accelerators: float
    fetalMovement: float
    uterineContractions: float
    lightDecelerations: float
    severeDeclerations: float
    prolonguedDecelerations: float


@app.get("/api/health")
def get_health():
    return {"status": "Up"}


@app.post("/api/new")
def return_prediction(data: FeotusData):
    # Do stuff
    print(data)

    # Return 0=Normal, 1=Suspect, 2=Pathological
    return {"result": 2}
