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

    abnormalShortTermVariability: float
    meanValueOfShortTermVariability: float
    percentageOfTimeWithAbnormalLongTermVariability: float
    meanValueOfLongTermVariability: float
    histogramWidth: float
    histogramMin: float
    histogramMax: float
    histogramNumberOfPeaks: float
    histogramNumberOfZeros: float
    histogramMode: float
    histogramMean: float
    histogramMedian: float
    histogramVariance: float
    histogramTendency: float


@app.get("/api/health")
def read_root():
    return {"status": "Up"}


@app.post("/api/new")
def read_item(data: FeotusData):
    # Do stuff
    print(data)

    # Return 0=Normal, 1=Suspect, 2=Pathological
    return {"result": 2}
