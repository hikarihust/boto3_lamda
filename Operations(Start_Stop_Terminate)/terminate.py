import boto3
client = boto3.client('ec2')

resp = client.terminate_instances(InstanceIds=['i-0519f3cf161a3c6b0'])

for instance in resp['TerminatingInstances']:
    print("The instance with id {} Terminated".format(instance['InstanceId']))