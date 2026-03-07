import pandas as pd

df = pd.read_csv("data/01.raw/complaints.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

df["date_received"] = pd.to_datetime(df["date_received"], errors="coerce")

df = df.dropna(subset=["date_received", "product", "issue", "state"])

df["product"] = df["product"].astype(str).str.strip()
df["issue"] = df["issue"].astype(str).str.strip()
df["state"] = df["state"].astype(str).str.upper().str.strip()

df["year_month"] = df["date_received"].dt.to_period("M").astype(str)

df.to_csv("data/02.processed/complaints_cleaned.csv", index=False)

print("Cleaned file saved successfully.")
print(df.head())