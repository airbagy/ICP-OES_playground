import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

file_path = "../data/ohio.csv"

df = pd.read_csv(file_path, index_col = 1)
df.drop("Wash3", axis=1, inplace=True)
df.drop("Mermet_ax", axis=1, inplace=True)

df[df.Analyte == "Fe 239.562"].plot()
plt.show()


df[['2ppm_Fe_ax', '20ppmFe_ax', '200ppmFe_ax']].plot()
plt.show() 
