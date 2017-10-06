from numpy.linalg import inv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulate import random_sim

''' This msf method does the training and predicting at the same time
'''

def msf(analt, itfrs, comb):
	 X = pd.concat(analt, itfrs)
	 Y = comb
	 b = np.dot(np.dot(inv(np.dot(X.transpose(), X)), X.transpose()), Y)
	 corrected = analt.multiply(b[0])
	 corrected.plot()
	 plt.title("Corrected analyte spectra")
	 plt.show()