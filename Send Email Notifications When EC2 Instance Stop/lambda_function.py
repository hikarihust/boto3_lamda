import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:us-east-2:954822992399:prod-alerts'
    message = 'Prod server stopped, please lookinto it'
    client.publish(TopicArn=topic_arn, Message=message)
    return 'Success'