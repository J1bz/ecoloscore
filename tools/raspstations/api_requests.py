# -*- coding: utf-8 -*-

from requests import requests
from json import loads

from conf import LOGIN, PASSWD, API


def get_token():
    login_data = {
        'username': LOGIN,
        'password': PASSWD,
    }
    login_url = '{}{}'.format(API['URL'], API['LOGIN_ROUTE'])
    r = requests.post(login_url, data=login_data)
    response = loads(r.content)
    token = response['token']
    return token


def get_auth_header(token):
    authorization = {
        'Authorization': 'Token {}'.format(token),
    }
    return authorization


def get_user_id(tag, auth_header):
    url_user_id = '{}{}?rfid_tag={}'.format(
        API['URL'],
        API['PROFILES_ROUTE'],
        tag,
    )
    r = requests.get(url_user_id, headers=auth_header)
    r_json = loads(r.content)
    if r_json:
        try:
            user_id = r_json[0]['user']
            return user_id

        except:
            pass

    return None


def check_position(user_id, arduino_id, auth_header):
    url_position = '{}{}'.format(
        API['URL'],
        API['CHECKS_ROUTE'],
    )
    position_data = {'user': user_id, 'point': arduino_id}
    requests.post(url_position, data=position_data, headers=auth_header)


def take_cup(user_id, auth_header):
    take_url = '{}{}'.format(
        API['URL'],
        API['TAKES_ROUTE'],
    )
    take_data = {'user': user_id}
    requests.post(take_url, data=take_data, headers=auth_header)


def throw_cup(user_id, auth_header):
    throw_url = '{}{}'.format(
        API['URL'],
        API['THROWS_ROUTE'],
    )
    throw_data = {'user': user_id}
    requests.post(throw_url, data=throw_data, headers=auth_header)
