# Batch Processing with Azure Databricks
This document outlines the steps to perform batch data processing using Azure Databricks with Spark. The use case involves reading a CSV file from Azure Data Lake Storage (ADLS), transforming the data, and writing it back in Parquet format.

# 📌 Prerequisites
 - Azure Databricks workspace
 - ADLS Gen2 
 - A CSV file uploaded to a source path
 - A cluster running with appropriate Spark runtime
 - Databricks notebook or job setup

# ⚙️ Environment Setup
 - Mount ADLS (if not already mounted)

# Steps in the workflow
 - Step 1: Read Input Data (CSV)
 - Step 2: Apply Data Transformation
 - Step 3: Write Output Data to a delta table or parquet file
 - Step 4: Validation


# 🔁 Optional: Automate Using Databricks Jobs
 - Create a new Job in Databricks.
 - Set the notebook path and cluster.
 - Configure a schedule (e.g., every day at midnight).
 - Add email alerts if needed.
