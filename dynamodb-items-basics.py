import boto3

# Table Name 
table_name = 'Movies'

# dynamodb client 
dynamodb_client = boto3.client('dynamodb')

# item_scarface 
item_scarface  = {
    'Title': {'S': 'Scarface'}
    ,'Year': {'S': '1983'}
}

 # get item

item_get ={
    'Title': {'S':'Scarface'}
    ,'Year': {'S': '1983'}
}

if __name__ == "__main__":

    # put item into db
    dynamodb_client.put_item(TableName = table_name, Item= item_scarface)

    
    # get item
    resp = dynamodb_client.get_item(TableName = table_name, Key = item_get)
    print(resp)
    print(resp['Item'])
    print(resp['Item']['Title']['S'])
