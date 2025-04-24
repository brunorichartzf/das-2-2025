import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

items = [
    {
        'cpf': {'S': '12345678900'},
        'nome': {'S': 'João da Silva'},
        'clienteativo': {'S': 'true'},
    },
     {
        'cpf': {'S': '12345678901'},
        'nome': {'S': 'João da Penha'},
        'clienteativo': {'S': 'true'},
    },
     {
        'cpf': {'S': '67890123456'},
        'nome': {'S': 'João da Laranjeira'},
        'clienteativo': {'S': 'true'},
    }
]

for item in items:
    try:
        dynamodb.put_item(
            TableName='cliente',
            Item=item
        )
        print(f"Item {item['cpf']['S']} inserted successfully.")
    except Exception as e:
        print(f"Error inserting item {item['cpf']['S']}: {e}")