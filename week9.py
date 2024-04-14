
import pandas as pd

# Create a DataFrame
data = {
    "Date": ["2023-01-01", "2023-01-01", "2023-01-02", "2023-01-02"],
    "Category": ["Electronics", "Furniture", "Electronics", "Furniture"],
    "Revenue": [1200, 1500, 1000, 900]
}

df = pd.DataFrame(data)

# Use the pivot method
pivot_df = df.pivot(index='Date', columns='Category', values='Revenue')

print(pivot_df)
