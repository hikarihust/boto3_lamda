def lambda_handler(event, context):
    resp = 'Hi {}, Welcome to Lambda'.format(event['name'])
    return resp
