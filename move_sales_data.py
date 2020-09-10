import json
import boto3
import os

dynamo = boto3.resource('dynamodb')

s3 = boto3.client('s3', aws_access_key_id=os.getenv(
    'ACCESS_KEY'), aws_secret_access_key=os.getenv('ACCESS_SECRET'))


def move_data_to_dynamo(event, context):
    game_bucket = event['Records'][0]['s3']['bucket']['name']
    bucket_key = event['Records'][0]['s3']['object']['key']
    s3_games = s3.get_object(Bucket=game_bucket, Key=bucket_key)[
        'Body'].read().decode('utf-8')
    s3_games_json = json.loads(s3_games)
    table = dynamo.Table(s3_games_json['DynamoDB_Table'])
    with table.batch_writer() as batch:
        for game in s3_games_json['data']:
            batch.put_item(Item=game)

    return {
        "statusCode": 200,
        "body": {
            "message": "success"
        }
    }
