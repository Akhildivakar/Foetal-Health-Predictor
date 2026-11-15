import torch


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