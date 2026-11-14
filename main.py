from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class FeotusData(BaseModel):
    baselineValue: float
    accelerators: float
    fetalMovement: float
    uterineContractions: float
    lightDecelerations: float
    severeDeclerations: float
    prolonguedDecelerations: float


@app.get("/api/health")
def read_root():
    return {"status": "Up"}


@app.post("/api/new")
def read_item(data: FeotusData):
    # Do stuff
    print(data)

    # Return 0=Normal, 1=Suspect, 2=Pathological
    return {"result": 2}
