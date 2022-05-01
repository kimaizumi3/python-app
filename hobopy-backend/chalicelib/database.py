import os
from turtle import title
from unittest import result
import uuid
import boto3 
from boto3.dynamodb.conditions import Key

 # ① DynamoDB への 接続 を 取得 する 
def _get_database(): 
    endpoint = os.environ.get("DB_ENDPOINT") 
    if endpoint:
        return boto3.resource("dynamodb", endpoint_url = endpoint)
    else:
        return boto3.resource("dynamodb")

# ② すべて の レコード を 取得 する 
def get_all_todos():
    table = _get_database().Table(os.environ["DB_TABLE_NAME"])
    response = table.scan()
    return response["Items"]

# ③指定されたID の レコード を 取得 する 
def get_todo(todo_id):
    table = _get_database().Table(os.environ["DB_TABLE_NAME"])
    response = table.query(
        KeyConditionExpression = Key("id").eq(todo_id)
    )
    items = response["Items"]
    return items[ 0] if items else None

# TODOを登録する
def create_todo(todo):
    # 登録内容の作成
    item = {
        'id': uuid.uuid4().hex,
        'title': todo['title'],
        'memo': todo['memo'],
        'priority': todo['priority'],
        'completed': False,
    }
    # DynamoDBにデータを登録
    table = _get_database().Table(os.environ['DB_TABLE_NAME'])
    table.put_item(Item=item)
    return item

# データ更新
def update_todo(todo_id, changes):
    table = _get_database().Table(os.environ['DB_TABLE_NAME'])
    update_expression = []
    expression_attribute_values = {}
    for key in ['title', 'memo', 'priority', 'completed']:
        if key in changes:
            # :={key[0:1]}は空白入れない。
            update_expression.append(f"{key} = :{key[0:1]}")
            expression_attribute_values[f":{key[0:1]}"] = changes[key]
    result = table.update_item(
        Key = {
            'id': todo_id,
            },
            UpdateExpression = 'set  ' + ','.join(update_expression),
            ExpressionAttributeValues = expression_attribute_values,
            ReturnValues = 'ALL_NEW'
    )
    return result['Attributes']

def delete_todo(todo_id):
    table = _get_database().Table(os.environ['DB_TABLE_NAME'])

    # DynamoDBのデータｗｐ削除
    result = table.delete_item(
        Key={
            'id': todo_id,
        },
        ReturnValues='ALL_OLD'
    )
    return result['Attributes']

