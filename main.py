import numpy as np
import pandas as pd

df = pd.read_csv("icici.csv")

df.drop(
    [
        "Price as on 31st Jan 2018",
        "Purchase Price Considered",
        "Purchase Value",
        "Sale Value",
        "Purchase Index Cost",
        "Profit/Loss(-)",
    ],
    axis=1,
    inplace=True,
)

df["Expenses"] = df["Purchase Expenses"] + df["Sale Expenses"]
df.drop(["Purchase Expenses", "Sale Expenses"], axis=1, inplace=True)

df["Sale Date"] = pd.to_datetime(df["Sale Date"], format="%d-%b-%y")
df["Sale Date"] = df["Sale Date"].dt.strftime("%d/%m/%Y")

df["Purchase Date"] = pd.to_datetime(df["Purchase Date"], format="%d-%b-%y")
df["Purchase Date"] = df["Purchase Date"].dt.strftime("%d/%m/%Y")

df["unlisted"] = np.nan
df["stt_paid"] = np.nan
df["FMV"] = np.nan

cols = [
    "ISIN",
    "Stock Symbol",
    "unlisted",
    "stt_paid",
    "Qty",
    "Purchase Date",
    "Purchase Rate",
    "Sale Date",
    "Sale Rate",
    "FMV",
    "Expenses",
]

df = df[cols]

template = pd.read_excel("template.xlsx", sheet_name="Stocks")

start = len(template)
writer = pd.ExcelWriter("template.xlsx", mode="a", if_sheet_exists="overlay")
df.to_excel(writer, sheet_name="Stocks", index=False, header=False, startrow=start + 1)
writer.close()
