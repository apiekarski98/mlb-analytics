import pandas as pd

# Load CSV
file = pd.read_csv("baseballdata.csv")

red_sox = file[file.Tm=='Boston Red Sox']
