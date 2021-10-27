import boto3
import json
import os
from math import ceil
import collections

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('syndeo-dev-regularizations-sms')
number_max_save_dynamodb = 25

try:
    with open(os.path.abspath(os.path.join(os.path.basename('.'), 'resources/result.json')), 'r') as file:
        lines_objets: list = json.load(file)

        data_group = []
        for loop in range(ceil(len(lines_objets) / number_max_save_dynamodb)):
            data_group.append(lines_objets[loop*number_max_save_dynamodb:(loop+1)*number_max_save_dynamodb])

        for data_loop in data_group:
            with table.batch_writer() as writer:
                for item in data_loop:
                    writer.put_item(Item=item)
except Exception as e:
    print(e)
