import numpy as np
import pandas as pd

csv_path = "/Users/ashoksharma/Local_Folder/pythonfiles/sea-reproduce/data/hepar2/hepar2.csv"   # update
out_npy  = "/Users/ashoksharma/Local_Folder/pythonfiles/sea-reproduce/data/hepar2/hepar2adj.npy"   # update

df = pd.read_csv(csv_path)
arr = df.to_numpy()
np.save(out_npy, arr)
print(arr.shape, "saved to", out_npy)
