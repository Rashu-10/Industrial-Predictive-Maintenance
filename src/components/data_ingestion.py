import pandas as pd

class DataIngestion:
  def initiate_data_ingestion(self):
    df=pd.read_csv("data/cleaned_data.csv")
    return df