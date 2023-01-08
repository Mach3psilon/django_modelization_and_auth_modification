import requests

def client():
    # credentials = {
    #     'username': '',
    #     'password': ''}

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #                             data=credentials)

    token_h = 'Token 21e4c819395d12a64e4e0b5da1bbfcfb547bf7f9'
    
    headers = {'Authorization': token_h}

    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)
    
    print('Status Code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()