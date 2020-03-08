import boto3  # import to pull AWS SDK for Python
import json  # import API for Python to work with JSON files
import time  # import time fucntions
s3_client = boto3.client('s3')  # creates low-level service client to AWS S3
dynamodb = boto3.resource('dynamodb')  # creates resource client to AWS DynamoDB


# When a .JSON file is added into the linked S3 bucket, another JSON file is created which contains
# the information about the S3 Bucket and the name of the file that was added to the bucket

def lambda_handler(event, context):
    print(str(event))

    # Print the JSON file created by S3 into CloudWatch Logs when an item is added into the bucket

    bucket = event['Records'][0]['s3']['bucket']['name']

    # Here the name of the S3 bucket is assigned to the variable 'bucket'
    # by grabbing the name from the JSON file created

    json_file_name = event['Records'][0]['s3']['object']['key']

    # Here the name of the file itself is assigned to the varibale 'json_file_name'
    # again by grabbing the name of the added file from the JSON file

    tname = json_file_name[:-5]
    # Defines the name of the table being added to dynamodb by using the name of S3 JSON file
    # *Use of [:.5] will strip the last five characters off the end of the file name

    print(tname)

    # Prints the name of the table into CloudWatch Logs

    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)

    # The json_object variable is assigned the values of the 'bucket' and the 'json_file_name'
    # This uses the boto3 client service and the rest of the script will reference the specified
    # S3 bucket and the JSON file that was added to the bucket

    jsonFileReader = json_object['Body'].read()

    # The jsonFileReader variable takes this object and read the body of JSON file

    jsonDict = json.loads(jsonFileReader)

    # Using the json.loads function, the arrays of the JSON file are converted into a string

    table = dynamodb.create_table(
        TableName=tname, ## Define table name from name of JSON file in S3
    KeySchema=[
        {
            'AttributeName': 'type', #Primary Key
            'KeyType': 'HASH'  #Partition Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'type',
            'AttributeType': 'S' #AttributeType N meas 'Number'
        }

    ],
    ProvisionedThroughput=
        {
            'ReadCapacityUnits': 10000,
            'WriteCapacityUnits': 10000
        }
    )
#    table.meta.client.get_waiter('table_exists').wait(TableName=tname)
    print(str(jsonDict))


    table.meta.client.get_waiter('table_exists').wait(TableName=tname)

    table = dynamodb.Table(tname)  # Specifies table to be used

    table.put_item(Item=jsonDict)  # Adds string of JSON file into the database
