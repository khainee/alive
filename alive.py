from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror, info as loginfo

BASE_URL = 'http://127.0.0.1'

if BASE_URL is not None:
    while True:
        try:
            res = rget(BASE_URL).status_code
            loginfo(f"success {res}")
            sleep(6)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
