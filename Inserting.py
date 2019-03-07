import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Course')

table.put_item(
   Item={
        'Service': 'S3',
        'Platform':'AWS',
        'Module 1': 'Overview	of	S3',
        'Module 2': ["Types	of	consistency	mode for distributed	storage" ,"S3’s	consistency	model", "Understanding	eventual consistenc"],
        'Module 3': 'S3 Namespace',
        'Module 4': 'Acess Control List',
        'Module 5': 'Bucket Policy',
        'Module 6': 'Multipart upload',
    }
)
print("inserted")
