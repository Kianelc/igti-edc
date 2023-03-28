import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-kiane-2023",
                        "raw-data/ITENS_PROVA_2020.csv",
                        "raw-data/ITENS_PROVA_2020.csv")

df = pd.read_csv("raw-data/ITENS_PROVA_2020.csv")

print(df)

s3_client.upload_file("raw-data/MICRODADOS_ENEM_2020.csv",
                      "datalake-kiane-2023",
                      "raw-data/MICRODADOS_ENEM_2020.csv")