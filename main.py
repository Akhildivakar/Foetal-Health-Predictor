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

class FourLayerFullyConnectedModelWithPReLU(torch.nn.Module):
  # Four-Layer fully connected model with PReLU
  def __init__(self):
    super().__init__()
    self.fc1 = torch.nn.Linear(21, 128)
    self.relu1 = torch.nn.PReLU()
    self.fc2 = torch.nn.Linear(128, 512)
    self.relu2 = torch.nn.PReLU()
    self.fc3 = torch.nn.Linear(512, 512)
    self.relu3 = torch.nn.PReLU()
    self.fc4 = torch.nn.Linear(512, 3)
  def forward(self, x):
    x = self.fc1(x)
    x = self.relu1(x)
    x = self.fc2(x)
    x = self.relu2(x)
    x = self.fc3(x)
    x = self.relu3(x)
    x = self.fc4(x)
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

model = FourLayerFullyConnectedModelWithPReLU()
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
