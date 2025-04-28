import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.update_item(
        TableName='cliente',
        Key={
            'cpf': {
                'S': '12345678900'
            }
        },
        UpdateExpression="SET clienteativo = :val",
        ExpressionAttributeValues={
            ':val': {'S': 'false'}
        },
        ReturnValues="UPDATED_NEW"
    )
    print("Item atualizado com sucesso:")
    print(resposta)
except Exception as e:
    print(f"Error: {e}")