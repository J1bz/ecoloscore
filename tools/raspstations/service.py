# -*- coding: utf-8 -*-
#!/usr/bin/python

from requests import requests
from re import compile, match
from serial import Serial
from utils import log
from api_requests import (get_user_id, check_position, take_cup, throw_cup,
                          get_token, get_auth_header)

from conf import TAG_REGEX, DEVICE, ARDUINOS, SCREEN


def handle_checkpoint(rfid_tag, arduino_id, api_auth_header):
    if SCREEN['ENABLED'] is True:
        requests.get(SCREEN['URL'])

    user_id = get_user_id(rfid_tag, api_auth_header)
    if user_id is not None:
        check_position(user_id, arduino_id, api_auth_header)


def handle_take(rfid_tag, api_auth_header):
    if SCREEN['ENABLED'] is True:
        requests.get(SCREEN['URL'])

    user_id = get_user_id(rfid_tag, api_auth_header)
    if user_id is not None:
        take_cup(user_id, api_auth_header)


def handle_throw(rfid_tag, api_auth_header):
    if SCREEN['ENABLED'] is True:
        requests.get(SCREEN['URL'])

    user_id = get_user_id(rfid_tag, api_auth_header)
    if user_id is not None:
        throw_cup(user_id, api_auth_header)


def start_service(serial_port, tag_c_regex, api_auth_header):
    while(True):
        try:
            line = serial_port.readline()

        except KeyboardInterrupt:
            log('Interruption : KeyboardInterrupt')
            exit()

        rfid_frame = match(tag_c_regex, line)

        if rfid_frame:
            arduino_id = int(rfid_frame.group(1))
            rfid_tag = rfid_frame.group(2) + rfid_frame.group(3) + \
                rfid_frame.group(4) + rfid_frame.group(5)

            log('tag nfc :' + rfid_tag)

            if arduino_id in ARDUINOS['stairs']:
                log("arduino " + str(arduino_id) + ": escalier")
                handle_checkpoint(rfid_tag, arduino_id, api_auth_header)

            elif arduino_id in ARDUINOS['cups']:
                log("arduino " + str(arduino_id) + ": gobelet")
                handle_take(rfid_tag, api_auth_header)

            elif arduino_id in ARDUINOS['bin']:
                log("arduino " + str(arduino_id) + ": poubelle")
                handle_throw(rfid_tag, api_auth_header)

            else:  # If arduino id is not known, we just pass...
                pass
                log('arduino inconnu')


if __name__ == '__main__':
    log('=== Starting service ecoloscore.service ===')

    tag_c_regex = compile(TAG_REGEX)

    token = get_token()
    auth_header = get_auth_header(token)

    serial_port = Serial(DEVICE, 115200, dsrdtr=0)

    start_service(serial_port, tag_c_regex, auth_header)
