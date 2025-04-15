# Automation script to run all notebooks in sequence

# Set notebook paths
notebook_paths = [
    "../notebooks/data_ingestion_and_cleaning",
    "../notebooks/data_transformation",
    "../notebooks/write_output",
    "../notebooks/validation"
]

# Execute notebooks sequentially
for notebook in notebook_paths:
    dbutils.notebook.run(notebook, 60)
