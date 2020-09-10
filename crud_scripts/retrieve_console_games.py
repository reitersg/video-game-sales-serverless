import os
import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')


def retrieve_console_games(event, context):
    table = dynamodb.Table(os.getenv('DYNAMO_TABLE'))

    result = table.scan(
        FilterExpression=Attr('platform').eq(
            event['pathParameters']['platform'])
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response
