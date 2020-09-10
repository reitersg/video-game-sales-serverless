import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')


def retrieve_all_games(event, context):
    table = dynamodb.Table(os.getenv('DYNAMO_TABLE'))

    result = table.scan()

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response
