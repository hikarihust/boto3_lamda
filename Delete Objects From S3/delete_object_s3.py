import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='javahomecloud123',
    Key='create_bucket.py'
)