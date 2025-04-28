import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.query(
        TableName='cliente',
        KeyConditionExpression='cpf = :cpf',
        ExpressionAttributeValues={
            ':cpf': {'S': '12345678900'}
        }
    )
    if "Items" in resposta and resposta["Items"]:
        print("Items encontrados:")
        for item in resposta["Items"]:
            print(item)
    else:
        print("Nenhum item encontrado.")
except Exception as e:
    print(f"Error: {e}")