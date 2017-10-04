import pandas as pd
from collections import OrderedDict
from sklearn.linear_model import LinearRegression
import numpy as np

def train_lr(df, wavelength):
    conc = np.array([2,20,200,700,1000,2000,10000]).reshape(-1,1)
    intensities = df.loc[wavelength]
    reg = LinearRegression()
    reg.fit(conc,intensities)
    return reg

def predict_lr(reg,conc):
    return reg.predict(conc)

