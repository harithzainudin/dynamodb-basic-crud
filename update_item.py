import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Books')

resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})
print("Before update")
print(resp['Item'])

print(" ")

# The UpdateItem API allows you to update a particular item as identified by its key.
resp = table.update_item(
    Key={"Author": "John Grisham", "Title": "The Rainmaker"},
    # Expression attribute names specify placeholders for attribute names to use in your update expressions.
    ExpressionAttributeNames={
        "#formats": "Formats",
        "#audiobook": "Audiobook",
    },
    # Expression attribute values specify placeholders for attribute values to use in your update expressions.
    ExpressionAttributeValues={
        ":id": "8WE3KPTP",
    },
    # UpdateExpression declares the updates you want to perform on your item.
    # For more details about update expressions, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
    UpdateExpression="SET #formats.#audiobook = :id",
)

resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})
print("After update")
print(resp['Item'])
