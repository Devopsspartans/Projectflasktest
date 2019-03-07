import boto3
from dynamo import putItem,getItem
priMkey="Id"
def data():
    Platform=input("Platform:")
    Id=input("Id:")
    Description=input("Description:")
    Service=("Service:")
    print("User Data")
    dynamodb = boto3.client('dynamodb', region_name="ap-south-1")
    tablename='Course'
    item = {"Platform":
                    {"S":Platform},
                "Id":
                    {"N" : Id },
                "Description" :
                    { "S" : Description},
                "Service" :
                    { "S" : Service },

        }

    putItem(tablename, item)
    #tab=getItem(tablename, priMkey,"Service")
    print(tab)

data()
print("Data inserted successfully!!")
