import boto3
import time

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    start_time = time.time()

    resposta = dynamodb.get_item(
        TableName='cliente',
        Key={
            'cpf': {
                'S': '12345678900'
            }
        }
    )

    end_time = time.time()
    elapsed_time = end_time - start_time 

    if "Item" in resposta:
        print("Item encontrado:")
        print(resposta["Item"])
    else:
        print("Item não encontrado.")

    print(f"Tempo para obter o item: {elapsed_time:.4f} segundos")
except Exception as e:
    print(f"Error: {e}")