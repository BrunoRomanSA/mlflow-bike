import pandas as pd
import boto3
import os

# Configuração do S3
s3_client = boto3.client('s3', region_name='us-east-1')
bucket_name = f"feature-store-bruno-data-bucket-{os.getenv('ENVIRONMENT')}"

# Carregar e tratar os dados
data = pd.read_csv("data/train.csv")

# Exemplo de tratamento
data['is_clear_weather'] = (data['weather'] == 1).astype(int)
data['is_rainy_weather'] = (data['weather'] >= 3).astype(int)


# Create a combined feature for holidays and working days
data['is_holiday_workingday'] = ((data['holiday'] == 1) & (data['workingday'] == 1)).astype(int)

# Convert 'datetime' column to datetime object
data['datetime'] = pd.to_datetime(data['datetime'])
# Create new features
data['hour'] = data['datetime'].dt.hour
data['day_of_week'] = data['datetime'].dt.dayofweek
data['month'] = data['datetime'].dt.month


data.drop(columns=["datetime"], inplace=True)

# Salvar os dados tratados localmente
output_file = "processed_data.parquet"
data.to_parquet(output_file, index=False)

# Fazer o upload para o S3
s3_client.upload_file(
    Filename=output_file,
    Bucket=bucket_name,
    Key="processed/processed_data.parquet"
)

print(f"Dados tratados enviados para s3://{bucket_name}/processed/processed_data.parquet")
# Limpar o arquivo local
os.remove(output_file)