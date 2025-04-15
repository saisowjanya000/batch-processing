# Notebook 3: Writing Data to Parquet

# Set output path
output_path = "/mnt/rawdata/processed/customers_parquet/"

# Write transformed data to Parquet
df_transformed.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(output_path)
