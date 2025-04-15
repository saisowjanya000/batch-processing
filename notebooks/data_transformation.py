# Notebook 2: Data Transformation

# Convert 'age' to integer and 'created_at' to timestamp
from pyspark.sql.functions import col

df_transformed = df_clean \
    .withColumn("age", col("age").cast("int")) \
    .withColumn("created_at", col("created_at").cast("timestamp"))

# Display the transformed dataframe
df_transformed.printSchema()
df_transformed.show(5)
