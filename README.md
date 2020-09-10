# video-game-sales-serverless
A serverless application that takes video game sales and puts them through S3 and DynamoDB using Lambda. Data is from Kaggle

# How it works

I use S3 Sync to upload the video game sales csv file to S3 to start off. Also, I made a custom plugin called "CustomPlugin" to trigger a lambda that converts the csv file to a json file for inserting into DynamoDB
After that, I kick off another lambda based on the json file being created in S3 that writes to DynamoDB all the video game sales. After that, I created two endpoints in API Gateway to retrieve all games and retrieve games based on their platform
(PS4, Wii, etc.)

The two endpoints are as followed:
/games_sales = retrieving all games
/games_sales/:platform = retrieving game sales based on game platform

# Deployment:

  - Install serverless locally and set up credentials from AWS for Serverless
  - Create an .env file with the following attributes: BUCKET_NAME - the S3 bucket name to use, DYNAMO_TABLE - Name of the DynamoDB table for the data to go into, ACCESS_SECRET & ACCESS_KEY - credentials from AWS IAM for whichever user
  - Run `npm install` to install serverless plugins
  - Finally, run `serverless deploy`

   
