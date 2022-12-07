import requests
from pprint import pprint

def client():

    credentials={
        'username':'aykhan',
        
        'password':'cirdaxanli213'
    }

    response=requests.post(
        url='http://127.0.0.1:8000/api/token/',data=credentials,)


    print('Status code',response.status_code)

    response_data=response.json()
    pprint(response_data)


if __name__ =='__main__':
    client()