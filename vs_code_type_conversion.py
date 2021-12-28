import pandas as pd

file_to_load = "201908-citibike-tripdata.csv"
citibike_df = pd.read_csv(file_to_load)

citibike_df["new_gender"] = citibike_df["gender"].astype(str)
citibike_df["new_gender"].replace({"0": "Unknown", "1": "Male", "2": "Female"}, inplace = True)

citibike_df.to_csv(r'c:\Users\17572\OneDrive\Desktop\DU_Data_Bootcamp\GitHub\bikesharing\citibike_df.csv', index = False)