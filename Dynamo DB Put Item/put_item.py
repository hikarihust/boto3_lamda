import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
table.put_item(
    Item={
        'id': '7',
        'name': 'kammana',
        'location': 'HN'
    }
)