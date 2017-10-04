import pandas as pd

df = pd.read_excel("ICP-OES_Dataset.xlsx")


cols = [2,4,6,8,10,12,14,16]
df.drop(df.columns[cols], axis=1, inplace=True) # Deleting repeating columns
df.columns = df.iloc[1] # Set column headers
df = df[df.Wavelength != "Wavelength"] # Remove repeating rows
df.reset_index(inplace=True) # Reset index
df.drop(df.columns[0], axis=1, inplace=True) # Remove useless column

# print(df.head())

df.to_csv('output.csv')
