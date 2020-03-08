import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket, Key=key)
    # The jsonFileReader variable takes this object and read the body of JSON file
    jsonFileReader = json_object['Body'].read()
    # Using the json.loads function, the arrays of the JSON file are converted into a string
    jsonDict = json.loads(jsonFileReader)
    table = dynamodb.Table('employees')
    table.put_item(Item=jsonDict)

    return "Hello from Lamda"
    
