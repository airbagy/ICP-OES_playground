import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import OrderedDict
import random

"""
In the study, full width at half max at 9pm. Spectra consists of 64 points with 2pm bw.

Shot noise

"""
def plot(sngl, add):
    plt.plot(add, label="Joined")
    for i, df in enumerate(sngl):
        plt.plot(df, label=str(i))

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.show()


def random_sim(n_simulations=2, rng=20, steps=0.01, add_noise=False):
    simulations = []
    combined = pd.DataFrame()

    x_axis = np.arange(-rng, rng, steps)

    for it in range(n_simulations):
        mean = random.randint(-rng,rng) # right value is also included
        sd = random.randint(1,4)
        sim = pd.DataFrame(index=x_axis, data={'y': norm.pdf(x_axis,mean, sd)})

        if add_noise:
            noise = np.random.normal(0,0.0001,[len(x_axis),1])
            sim += noise

        simulations.append(sim)
        if not combined.empty:
            combined = combined + sim
        else:
            combined = sim.copy()
    return simulations, combined


#sims, comb = random_sim(n_simulations=3, steps=0.001,rng=20, add_noise=True)
#plot(sims,comb)