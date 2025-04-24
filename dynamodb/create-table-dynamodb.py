import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    dynamodb.create_table(
        TableName='cliente',
        KeySchema=[
            {
                'AttributeName': 'cpf',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'cpf',
                'AttributeType': 'S'  # String type
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Table 'cliente' created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")