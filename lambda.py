import pandas as pd

def Lambda_handler(event, context):
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    
    summary = df.describe()
    print("\nSummary Statistics:")
    print(summary)
    
    return {
        'statusCode': 200,
        'body': 'Data processed successfully'
    }