def add_features(df):
    df['TX_HOUR'] = df['TX_DATETIME'].dt.hour
    df['TX_DAY'] = df['TX_DATETIME'].dt.day
    df['TX_MONTH'] = df['TX_DATETIME'].dt.month
    return df
