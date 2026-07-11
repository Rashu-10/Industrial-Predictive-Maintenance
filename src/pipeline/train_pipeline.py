from src.components.data_ingestion import DataIngestion

dataset=DataIngestion()

df=dataset.initiate_data_ingestion()

print(df.head())