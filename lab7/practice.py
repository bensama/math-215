import pandas as pd
import numpy as np
from google.colab import files
import io

uploaded = files.upload()

df = pd.read_csv(io.StringIO(uploaded['Lab7data.csv'].decode('utf-8')))
signal_data = df.values
signal_data

print(np.shape(signal_data))