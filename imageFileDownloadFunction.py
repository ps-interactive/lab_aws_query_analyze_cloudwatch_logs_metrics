import time 

def lambda_handler(event, context): 
    download_time = event['downloadTime'] 
     
    print('File download started') 

    file_size = 500 + download_time

    time.sleep(download_time) 

    if download_time > 10: 
        print('File type is PNG RequestId: ' + context.aws_request_id) 
    else: 
        print('File type is JPEG RequestId: ' + context.aws_request_id)
     
    print('File download completed') 
    print('File size: ' + str(file_size) + ' KB RequestId: ' + context.aws_request_id) 

    return { 
        'statusCode': 200, 
        'body': 'File download successful' 
    }