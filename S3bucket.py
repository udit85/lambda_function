import boto3 

def lambda_handler(event, context): 
  bucket_name = 'YOUR_BUCKET_NAME' 
  file_name = 'file_name.txt' 
  file_content = 'This is the content of the file.' 

  s3 = boto3.client('s3') 
  s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_name) 
  return { 
      'statusCode': 200, 
      'body': 'File uploaded successfully.' 
  }