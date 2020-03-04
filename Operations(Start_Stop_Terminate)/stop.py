import boto3
client = boto3.client('ec2')

resp = client.stop_instances(InstanceIds=['i-0519f3cf161a3c6b0'])
