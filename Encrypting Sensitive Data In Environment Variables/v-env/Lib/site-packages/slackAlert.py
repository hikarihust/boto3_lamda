import requests 
import json
import os
import boto3
from base64 import b64decode

ENCRYPTED = os.environ['SLACK_WEBHOOK']
keyId = 'arn:aws:kms:us-east-2:954822992399:key/0e629e50-d8ad-4455-acd2-cdd5fa39021d'
kms = boto3.client('kms')

slack_web_hook = kms.decrypt(
    CiphertextBlob = b64decode(ENCRYPTED),
    KeyId = keyId,
    EncryptionAlgorithm = 'SYMMETRIC_DEFAULT'
)['Plaintext']

def send_lack(event, context):
    print(str(event))
    slack_message = { 'text': 'EC2 Instance Stopped' }
    resp = requests.post(slack_web_hook, data = json.dumps(slack_message))
    return resp.text