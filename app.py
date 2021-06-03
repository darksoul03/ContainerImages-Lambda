import json
from sklearn.datasets import load_iris
import pandas as pd
def lambda_handler(event, context):
    iris_dataset = load_iris()
    iris_data=iris_dataset['data']
    iris_df=pd.DataFrame(iris_data)
    c=iris_df.head()
    print(c)
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Output is ",
                            "event": c})
    }
