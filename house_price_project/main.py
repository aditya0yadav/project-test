import pandas as pd
from datetime import datetime
import os

# Ensure the directory exists
os.makedirs("feature_repo/data", exist_ok=True)

# Create the DataFrame
data = pd.DataFrame({
    "house_id": [1, 2, 3],
    "location": ["city_center", "suburb", "rural"],
    "size_sqft": [1000, 1500, 1200],
    "bedrooms": [2, 3, 2],
    "age": [5, 10, 20],
    "price_per_sqft": [500.0, 300.0, 200.0],
    "is_luxury": [1, 0, 0],
    "age_bucket": ["new", "mid", "old"],
    "event_timestamp": [datetime.now()] * 3,
})

# Save as Parquet in the correct folder
data.to_parquet("feature_repo/data/house_data.parquet")
