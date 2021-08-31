import requests
import time
from . import aes
import json


HEADERS = {
    'content-type':'application/json',
}


class SasAPI():

    def __init__(self):
        self.base_url = 'http://demo4.sasradius.com/user/api/index.php/api/'
        self.session = requests.Session()
        self.session.headers = HEADERS


    def login(self, username, password):
        route = 'auth/login'
        payload = aes.encrypt(json.dumps({
            'username': username,
            'password': password
        }))
        data = {
            'payload': payload,
        }
        login_url = self.base_url + route
        response = self.session.post(login_url, json=data)
        if response.status_code != 200:
            return {'status': response.status_code}
            
        return response.json()

    def restorePassword(self, email):
        route = 'auth/restorePassword'
        payload = aes.encrypt(json.dumps({
            'email': email,
        }))
        data = {
            'payload': payload,
        }
        login_url = self.base_url + route
        response = self.session.post(login_url, json=data)
        if response.status_code != 200:
            return {'status': response.status_code}
            
        return response.json()


    def usage(self, token):
        # {"report_type":"daily","month":1,"year":2021,"user_id":null}
        # {"report_type":"monthly","month":"12","year":"2020","user_id":null}
        route = 'traffic'
        self.session.headers['Authorization'] = f'Bearer {token}'
        payload = aes.encrypt(json.dumps({
            'report_type': 'daily',
            'month': 1,
            'year': 2021,
            'user_id': None,
        }))
        data = {
            'payload': payload,
        }
        login_url = self.base_url + route
        response = self.session.post(login_url, json=data)
        if response.status_code != 200:
            return {'status': response.status_code}
            
        return response.json()

    def redeem(self, pin, token):
        route = 'redeem'
        self.session.headers['Authorization'] = f'Bearer {token}'
        payload = aes.encrypt(json.dumps({
            'pin': pin,
        }))
        data = {
            'payload': payload,
        }
        login_url = self.base_url + route
        response = self.session.post(login_url, json=data)
        print(response.text)
        if response.status_code != 200:
            return {'status': response.status_code}
            
        return response.json()

    def details(self, token):
            route = 'user'
            user_url = self.base_url + route
            self.session.headers['Authorization'] = f'Bearer {token}'
            response = self.session.get(user_url)
            return response.json()
