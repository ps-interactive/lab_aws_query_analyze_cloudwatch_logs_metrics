import time 

def lambda_handler(event, context): 
    download_time = event['downloadTime'] 
     
    print('File download started') 
     
    file_size = download_time * 50 
     
    time.sleep(download_time) 
    
    print('File type is PDF RequestId: ' + context.aws_request_id) 
    print('File download completed RequestId: ' + context.aws_request_id) 
    print('File size: ' + str(file_size) + ' KB RequestId: ' + context.aws_request_id) 

    return { 
        'statusCode': 200, 
        'body': 'File download successful' 
    }