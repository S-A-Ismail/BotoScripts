import boto3
import pandas as pd

def list_databases():
    Catalog = boto3.client('glue', region_name='<Insert Region>')
    DatabaseList = []
    starting_token = ""
    next_page = True
    while next_page:
        response = Catalog.get_databases(
        CatalogId='<Insert Catalog>',
        ResourceShareType='ALL',
        NextToken= starting_token,
        MaxResults=500
        )
        for Database in response["DatabaseList"]:
            DatabaseList.append(Database["Name"])
        starting_token = response.get('NextToken')
        if starting_token is None:
            break
    return DatabaseList

def list_table_columns(Database):
    Catalog = boto3.client('glue', region_name='<Insert Region>')
    start_token = ""
    TableList = []
    while True:
        response = Catalog.get_tables(DatabaseName = Database, NextToken = start_token)
        for tables in response['TableList']:
            for columns in tables['StorageDescriptor']['Columns']:
                TableList.append(tables['Name'] + '.' + columns['Name'])
        start_token = response.get('NextToken')
        if start_token is None:
            break
    return TableList

ListDatabases = list_databases()
with open("GlueSchemas.txt", "w") as f:
    for Database in ListDatabases:
        ListTable =  list_table_columns(Database)
        for table in ListTable:
            f.write(str(Database) + ',' + str(table) + ',\n')



