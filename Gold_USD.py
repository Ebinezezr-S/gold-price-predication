import pandas as pd
import yfinance as yf
from prophet import Prophet
import matplotlib.pyplot as plt

# Step 1: Download gold futures in USD
gold_usd = yf.download("GC=F", start="2023-01-01", end="2025-01-01")

# Step 2: Download USD/INR exchange rate
usd_inr = yf.download("USDINR=X", start="2023-01-01", end="2025-01-01")

# Step 3: Combine into one DataFrame
df = pd.concat([gold_usd['Close'], usd_inr['Close']], axis=1)
df.columns = ['Gold_USD', 'USDINR']   # ✅ Clean column names

# Step 4: Reset index so Date becomes a column
df = df.reset_index()

# Step 5: Compute Gold price in INR
df['Gold_INR'] = df['Gold_USD'].astype(float) * df['USDINR'].astype(float)

# Step 6: Prophet format
df = df[['Date', 'Gold_INR']].rename(columns={"Date": "ds", "Gold_INR": "y"})
print(df.head(), df.shape)

# Step 7: Fit Prophet
model = Prophet(daily_seasonality=True)
model.fit(df)

# Step 8: Forecast next 365 days
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Step 9: Plot forecast
fig1 = model.plot(forecast)
plt.show()

fig2 = model.plot_components(forecast)
plt.show()
