import os
import pandas as pd

def load_data(directory="dataset/data/"):
    dataframes = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".pkl"):
            file_path = os.path.join(directory, filename)
            df = pd.read_pickle(file_path)
            dataframes.append(df)

    if not dataframes:
        raise FileNotFoundError(f"No .pkl files found in directory: {directory}")

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

def preprocess_data(df):
    df['TX_DATETIME'] = pd.to_datetime(df['TX_DATETIME'])
    df.sort_values(by='TX_DATETIME', inplace=True)
    return df
