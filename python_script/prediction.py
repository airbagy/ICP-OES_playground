import pandas as pd
import matplotlib.pyplot as plt
from pred import train_lr, predict_lr

pd.options.mode.chained_assignment = None

all_elems = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
             'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar','K', 'Ca', 
             'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 
             'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 
             'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 
             'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 
             'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 
             'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra',
             'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 
             'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Ce', 'Pr', 
             'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 
             'Tm', 'Yb', 'Lu', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 
             'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'] # A list of all elements
file_path = "../data/ohio.csv"

# Get a dataframe of spectra
df = pd.read_csv(file_path, index_col = 1)
df.drop("Wash3", axis=1, inplace=True)
df.drop("Mermet_ax", axis=1, inplace=True)

# Selection of analyte
analt = input("Please select the analyte: ")
while analt not in all_elems:
	analt = input("Please select a valid element name: ")
print("The analyte you have selected is: " + analt)

# Selection of peak of interest
analts = df["Analyte"].drop_duplicates()
peaks = [] # List of wavelengths for user to choose from
peak = ""
for elem in analts:
	if elem.split(' ')[0] == analt:
		peaks.append(elem)
if len(peaks) == 0:
	print("Unfortunately our instrument does not support detection of this element.")
	exit(0)
else: 
	print("There are " + str(len(peaks)) + " emission peaks of " + analt)
	for i in range(0, len(peaks)):
		print(str(i+1) + ". " + peaks[i])
try:
    num = int(input("Please select the wavelength of interest(index): "))-1
    peak = peaks[num]
except ValueError:
    print("Not an integer value...")
except IndexError:
	print("Not in range...")

# Prediction
conc = 0
try:
    conc = int(input("Please select concentration of Fe you want(ppm): "))
except ValueError:
    print("Not an integer value...")

print("Please hold, prediction may take some time.")
rf_box = df[df.Analyte == peak]      
rf_box.drop('Analyte', axis=1, inplace=True) # Cleaned up the data
wlens = rf_box.index.values
concs = []
for wlen in wlens:
	reg = train_lr(rf_box, wlen)
	concs.append(predict_lr(reg, conc)[0])

# Result and plotting

result = pd.DataFrame({
	'Wavelength': wlens,
	'Concentration': concs
})
result.set_index('Wavelength', inplace=True)
result.plot()
plt.show()