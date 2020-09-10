import csv
import boto3
import os
import uuid
import json
s3 = boto3.client('s3', aws_access_key_id=os.getenv(
    'ACCESS_KEY'), aws_secret_access_key=os.getenv('ACCESS_SECRET'))


def aggregate_data_by_console(event, context):
    video_game_obj = s3.get_object(
        Bucket=os.getenv('BUCKET_NAME'), Key='vgsales.csv')
    video_game_sales = video_game_obj['Body'].read().decode(
        'utf-8').splitlines(True)
    aggregated_data = list()
    data = csv.DictReader(video_game_sales)
    for row in data:
        entry = game_console(row=row)
        aggregated_data.append(entry)
    s3.put_object(Body=json.dumps({"DynamoDB_Table": 'VideoGames', "data": aggregated_data}), Bucket=os.getenv(
        'BUCKET_NAME'), Key="processed/vgsales.json")
    return json.dumps({
        "statusCode": 200,
        "body": {
            "message": "success"
        }
    })


def game_console(row):
    return {
        '_id': str(uuid.uuid4()),
        'name': row['Name'],
        'platform': row['Platform'],
        'year_published': row['Year'],
        'genre': row['Genre'],
        'NA_sales': row['NA_Sales'],
        'EU_Sales': row['EU_Sales'],
        'Global_Sales': row['Global_Sales']
    }
