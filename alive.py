from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror, info as loginfo

BASE_URL = 'http://localhost'

if BASE_URL is not None:
    while True:
        try:
            rget(BASE_URL).status_code
            loginfo("success")
            sleep(6)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
