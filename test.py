import boto3

dynamodb = boto3.resource('dynamodb')
#table = dynamodb.Table('course')

"""response = table.get_item(
    Key={
        1 : 1
    }
)

item = response['Item']
name = item['Service']

print(item) 
print("Course : {}".format(name))
"""
table = dynamodb.create_table(
    TableName='Course',
    KeySchema=[
        {
            'AttributeName': 'Service',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Platform',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Platform',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Service',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
print("DONE")
table.meta.client.get_waiter('table_exists').wait(TableName='users')
print(table.item_count)



