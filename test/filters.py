import math
import numpy as np

def lowpass(data, alpha):
  filtered = [data[0]]
  for i in range(1, len(data)):
    filtered.append((1 - alpha) * filtered[i-1] + alpha * data[i])
  return filtered
