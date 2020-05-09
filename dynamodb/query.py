import boto3
from boto3.dynamodb.conditions import Key
import decimal
import json

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

tablename = "northwind"
dynamodb = boto3.resource('dynamodb', region_name="ap-southeast-1")
table = dynamodb.Table(tablename)

def getJsonItems(item):
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))


# a. Get employee by employee ID
# response = table.query(KeyConditionExpression=Key('pk').eq('employees#2'))
# getJsonItems(response['Items'])

# b. Get direct reports for an employee
# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('employees#2'))
# getJsonItems(response['Items'])

# # c. Get discontinued products
# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('PRODUCT') & Key('data').eq('1'))
# getJsonItems(response['Items'])

# # d. List all orders of a given product
response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('products#1'))
getJsonItems(response['Items'])

# # e. Get the most recent 25 orders
# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('ORDER'), Limit=25)
# print(response['Items'])

# # f. Get shippers by name
# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('United Package'))
# print(response['Items'])

# # g. Get customers by contact name
# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('Maria Anders'))
# print(response['Items'])

# # h. List all products included in an order
# response = table.query(KeyConditionExpression=Key('pk').eq('10260') & Key('sk').begins_with('product'))
# print(response['Items'])

# # i. Get suppliers by country and region
# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('SUPPLIER') & Key('data').begins_with('Germany#NULL'))
# print(response['Items'])