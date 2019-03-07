import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Course')

response = table.query(
    KeyConditionExpression = Key('Platform').eq('AWS')
)
result1 = response['Items']
print(result1)
for i in response['Items']:
    print(i['Platform'],",",i['Service'])
