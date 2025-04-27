from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64, String
from datetime import timedelta
from feast import FileSource
from feast import ValueType


house_data = FileSource(
    path="data/house_data.parquet",
    timestamp_field="event_timestamp",
)

house = Entity(name="house_id", value_type=ValueType.INT64, join_keys=["house_id"])


house_features = FeatureView(
    name="house_features",
    entities=[house],
    fields=[
        Field(name="location", dtype=ValueType.STRING),
        Field(name="size_sqft", dtype=ValueType.INT32),
        Field(name="bedrooms", dtype=ValueType.INT32),
        Field(name="age", dtype=ValueType.INT32),
        Field(name="price_per_sqft", dtype=ValueType.FLOAT),
        Field(name="is_luxury", dtype=ValueType.INT32),
        Field(name="age_bucket", dtype=ValueType.STRING),
    ],
    batch_source=your_batch_source,  # Make sure the batch source is defined here
)

