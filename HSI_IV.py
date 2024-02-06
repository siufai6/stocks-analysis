import pandas as pd
#import numpy as np
#import datetime as dt

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

VIX_FILE = "./HSIL.csv"
HSI_FILE="./HSI.csv"

print("reading data from VIX file {}".format(VIX_FILE))

vix_df = pd.read_csv(VIX_FILE)

vix_df=vix_df[['Date','Close']]

vix_df=vix_df.rename(columns={"Close": "ImplVol"})

vix_df['Date']=pd.DatetimeIndex(vix_df['Date'])
print(vix_df)


print("reading data from HSI quotes file {}".format(HSI_FILE))

ohlc = pd.read_csv(HSI_FILE)

ohlc['Date'] = pd.DatetimeIndex(ohlc['Date'])
print(ohlc)
combined = ohlc.set_index('Date').join(vix_df.set_index('Date'),how='inner')
print(combined)

# we normalize the HSI index and VIX so the observation (divergence) is more obvious
combined = normalize(combined)


import plotly.graph_objects as go
from plotly.subplots import make_subplots
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=combined.index, y=combined['Close'],
                    mode='lines',
                    name="HSI", line=dict(color="#000000")), secondary_y=True)


fig.add_trace(go.Scatter(x=combined.index, y=combined['ImplVol'],
                    mode='lines',
                    name='Implied Volatility', line=dict(color="#ff0000")),
                    secondary_y=False)


fig.update_layout(hovermode='x unified')

import plotly.io as pio
fig.write_html("./sentiment_HSI.html")

