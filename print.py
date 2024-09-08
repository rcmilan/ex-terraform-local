import boto3

def list_dynamodb_tables():
    # Connect to the local DynamoDB instance using Boto3
    dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:4566')

    # List all tables
    response = dynamodb.list_tables()

    # Print all table names
    if 'TableNames' in response:
        print("Tables in DynamoDB:")
        for table in response['TableNames']:
            print(table)
    else:
        print("No tables found.")

if __name__ == "__main__":
    list_dynamodb_tables()
