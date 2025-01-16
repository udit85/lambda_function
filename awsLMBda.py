import json

def lambda_handler(event, context):
    try:
        num1 = event['num1']
        num2 = event['num2']
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing num1 or num2 in the request.'})
        }