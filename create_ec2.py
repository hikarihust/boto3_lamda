import boto3
ec2 = boto3.resource('ec2', region_name='us-east-2')

ec2.create_instances(ImageId='ami-0e38b48473ea57778', MinCount=1, MaxCount=1, InstanceType='t2.micro')