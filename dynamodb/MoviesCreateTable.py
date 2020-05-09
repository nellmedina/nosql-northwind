from __future__ import print_function # Python 2/3 compatibility
import boto3

# dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1', endpoint_url="http://localhost:8000")

# dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb = boto3.client('dynamodb', region_name='ap-southeast-1')

table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# table = dynamodb.Table('Movies')
# table.delete()

print("Table status:", table.table_status)