import boto3
ec2 = boto3.resource('ec2', region_name='us-east-2')

ec2.create_instances(ImageId='ami-0d8f6eb4f641ef691', MinCount=1, MaxCount=1, InstanceType='t2.micro')