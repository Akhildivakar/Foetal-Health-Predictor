import torch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import FourLayerFullyConnectedModelWithPReLU

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

model = FourLayerFullyConnectedModelWithPReLU()
model.load_state_dict(torch.load("./model.pth", map_location="cpu"))
model.eval()

@app.get("/api/health")
def get_health():
    return {"status": "Up"}

@app.post("/api/new")
def return_prediction(data: FeotusData):
    x_input = [data.baselineValue, data.accelerators, data.fetalMovement, data.uterineContractions, data.lightDecelerations, data.severeDeclerations, data.prolonguedDecelerations, data.abnormalShortTermVariability, data.meanValueOfShortTermVariability, data.percentageOfTimeWithAbnormalLongTermVariability, data.meanValueOfLongTermVariability, data.histogramWidth, data.histogramMin, data.histogramMax, data.histogramNumberOfPeaks, data.histogramNumberOfZeros, data.histogramMode, data.histogramMean, data.histogramMedian, data.histogramVariance, data.histogramTendency]
    
    pred = model(torch.tensor(x_input))
    
    probabilities = torch.nn.functional.softmax(pred, dim=1)
    return {"probabilities": probabilities}
