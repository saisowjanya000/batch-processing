# Notebook 1: Data Ingestion and Initial Cleaning

# Set input data path
input_path = "/mnt/rawdata/source_data/customers.csv"

# Read data from CSV
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(input_path)

# Display first 5 rows to inspect
df.show(5)

# Filter rows where 'age' is not null
df_clean = df.filter(col("age").isNotNull())
df_clean.show(5)
