import pandas as pd
# Initialize an empty dictionary
data_dict = {}

def read_data():
    df = pd.read_csv('Data/fingerprint characteristic data.csv')
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # If the filename is not already a key in the dictionary, add it with an empty list as its value
        if row['filename'] not in data_dict:
            data_dict[row['filename']] = []
        # Append the values as a list to the filename key in the dictionary
        data_dict[row['filename']].append([row['start_points'], row['connection_points'], row['branch_points']])
