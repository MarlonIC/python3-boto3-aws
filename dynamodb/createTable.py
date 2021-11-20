import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='personal', region_name='us-east-1')
client = session.client('dynamodb')

try:
    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'userId',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            }
        ],
        TableName='table-users',
        KeySchema=[
            {
                'AttributeName': 'userId',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'email',
                'KeyType': 'RANGE'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

    status = response.get('TableDescription').get('TableStatus')
    # El estado será siempre CREATING porque el proceso de
    # creación de una tabla mediante python es asincrono
    print('Estado de creación de la tabla', status)
    print('response', response)
except ClientError as clientError:
    print(clientError.response['Error']['Message'])
    # print(clientError.response)8
except Exception as error:
    print(error)
