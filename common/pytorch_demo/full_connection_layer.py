import torch
import torch.nn as nn

x = torch.randint(0, 255,  (1, 128*128), dtype=torch.float32)
fc = nn.Linear(128*128, 2)
y = fc(x)

print(y)
output = nn.Softmax(dim=1)(y)
print(output)
