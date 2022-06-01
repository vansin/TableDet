from re import M
import torch
import torch.nn as nn

y = torch.randn(3)

print(y)

m = nn.Softmax(dim=0)
out = m(y)
print(out)