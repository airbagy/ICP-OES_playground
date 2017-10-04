import pandas as pd
from io import StringIO
import sys
import matplotlib.pyplot as plt
from collections import OrderedDict

path = "ICP-OES_First_Clean.csv"
output = "ohio.csv"


def _get_columns(line):
    cols = line.split(',')
    cols.insert(0, 'Analyte')
    cols[-1] = cols[-1].strip('\n') # Remove newline from last column.
    cols = [col.replace(' ', '_') for col in cols] # add underscore insteaad of space
    return cols


def preprocess(path):
    s = StringIO()
    cur_analyte = None
    with open(path) as f:
        cols = _get_columns(f.readline())
        for ln in f:
            if not ln.strip(','):
                continue # continue on empty line
            if ln.startswith('Analyte'):
                cur_analyte = ln.split(',')[1] + ',' # Get analyte
                continue
            s.write(cur_analyte + ln)
        s.seek(0) # reset buffer to the beginning of the StringIO object
    df = pd.read_csv(s, names=cols, header=None)
    return  df

df = preprocess(path)
df.to_csv(output, index=False)

def plot(df):
    df[['2ppm_Fe_ax', '20ppmFe_ax', '200ppmFe_ax']].plot() #
    plt.show()


df = pd.read_csv(path, index_col=1)


fe = df[df.Analyte.str.startswith('Fe')].drop('Analyte', axis=1).sort_index()
notiron = df[~df.Analyte.str.startswith('Fe')].drop('Analyte', axis=1).sort_index()
plt.plot(notiron[['2ppm_Fe_ax']], label='other')
df =  df.drop('Analyte', axis=1).sort_index()
plt.plot(df['2ppm_Fe_ax'])
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.show()
plot(fe)
#pb = df[df.Analyte == 'Pb 261.418'] #or df.Analyte == 'Pb 283.306']
#fe = df[df.Analyte == 'Fe 259.939'] or df.Analyte == 'Fe 273.955']


plt.show()

#br = df[df.Analyte == 'Br 163.280']

#pb = df[df.Analyte.str.startswith('Pb')].drop('Analyte',axis=1).sort_index()
#fe = df[df.Analyte.str.startswith('Fe')].drop('Analyte', axis=1).sort_index()
