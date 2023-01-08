import requests

def client():
    data = {
        'username': 'resttest',
        'email': 'test@rest.com',
        'password1': 'change123',
        'password2': 'change123'
        }

    response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
                                data=data)

    # token_h = 'Token f0968a384445f529248433dd9af87e2ada41717a'
    
    # headers = {'Authorization': token_h}

    # response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)
    
    print('Status Code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()