import boto3
import json
import time

aws_access_key_id = input("Enter the AWS access key ID for your sandbox: ")
aws_secret_access_key = input("Enter the AWS secret access key for your sandbox: ")

client = boto3.client(
    'lambda',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

i = 1

while (5 >= i):
    # CloudWatch metrics resolution is 1 minute by default and doesn't go lower than that unless you create custom metrics
    time.sleep(60)
    
    downloadTime = i * 10

    response = client.invoke(
        FunctionName = 'textFileDownloadFunction',
        Payload = json.dumps({"downloadTime": downloadTime})
    )

    # response from textFileDownloadFunction
    response_payload = response['Payload']
    response_payload_plain = response_payload.read()

    print(response_payload_plain)

    i += 1