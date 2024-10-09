from dotenv import load_dotenv
import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Carregando as chaves de acesso a partir das variáveis de ambiente
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_name = os.getenv('S3_BUCKET_NAME')
kms_key_id = os.getenv('KMS_KEY_ID')

# Configurando o cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

file_name = 'file_to_upload.txt'
directory_name = 'carteirinha/2024/sept/'  # Especificando o "diretório"

try:
    # Subir um arquivo para o bucket com criptografia KMS
    s3.upload_file(
        Filename=file_name,
        Bucket=bucket_name,
        Key=f'{directory_name}{file_name}',
        ExtraArgs={
            'ServerSideEncryption': 'aws:kms',
            'SSEKMSKeyId': kms_key_id
        }
    )
    print(f'{file_name} uploaded successfully to {bucket_name} with KMS encryption')
except FileNotFoundError:
    print('The file was not found')
except NoCredentialsError:
    print('Credentials not available')
except ClientError as e:
    print(f'Error uploading file: {e}')
