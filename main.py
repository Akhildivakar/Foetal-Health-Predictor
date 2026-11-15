import torch
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

class FiveLayerFullyConnectedModelWithPReLUAndDropout(torch.nn.Module):
  # Five-Layer fully connected model with PReLU and Dropout layers
  def __init__(self):
    super().__init__()
    self.stack = torch.nn.Sequential([
        torch.nn.Linear(21, 128),
        torch.nn.PReLU(),
        torch.nn.Dropout(0.5),
        torch.nn.Linear(128, 512),
        torch.nn.PReLU(),
        torch.nn.Dropout(0.5),
        torch.nn.Linear(512, 512),
        torch.nn.PReLU(),
        torch.nn.Dropout(0.5),
        torch.nn.Linear(512, 128),
        torch.nn.PReLU(),
        torch.nn.Dropout(0.5),
        torch.nn.Linear(128, 3)
    ])
  def forward(self, x):
    x = self.stack(x)
    return x

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

model = FiveLayerFullyConnectedModelWithPReLUAndDropout()
model.load_state_dict(torch.load("./model.pth", weights_only=False))
model.eval()

@app.get("/api/health")
def get_health():
    return {"status": "Up"}

@app.post("/api/new")
def return_prediction(data: FeotusData):
    x_input = [data.baselineValue, data.accelerators, data.fetalMovement, data.uterineContractions, data.lightDecelerations, data.severeDeclerations, data.prolonguedDecelerations, data.abnormalShortTermVariability, data.meanValueOfShortTermVariability, data.percentageOfTimeWithAbnormalLongTermVariability, data.histogramWidth, data.histogramMin, data.histogramMax, data.histogramNumberOfPeaks, data.histogramNumberOfZeros, data.histogramMode, data.histogramMean, data.histogramMedian, data.histogramVariance, data.histogramTendency]
    
    pred = model(x_input)
    
    probabilities = pred.softmax()
    return {"probabilities": probabilities}
