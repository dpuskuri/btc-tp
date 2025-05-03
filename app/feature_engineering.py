import pandas as pd

def add_features(df):
    df["vol_ma"] = df["volume"].rolling(window=20).mean()
    df["volume_spike"] = df["volume"] > df["vol_ma"] * 2

    # Simple consolidation logic
    df['consolidation'] = df['close'].rolling(window=10).apply(
        lambda x: (x.max() - x.min()) / x.min() < 0.005)

    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
    df.dropna(inplace=True)
    return df
