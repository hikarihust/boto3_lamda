import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
resp = table.get_item(
    Key={
        'id': '7'
    }
)

print(resp['Item'])