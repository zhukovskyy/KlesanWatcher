import urllib.request
import os

import pytest
from slacker import Slacker


def test_slack_api_key():
    slack_api_key = os.environ.get('SLACK_API')
    slack = Slacker(slack_api_key)
    slack.chat.post_message('#klesan_log', 'test slack api key')


def test_cwb_api_key():
    APP_KEY = os.environ.get('CWB_API', None)
    url = 'http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=F-D0047-1' % APP_KEY
    response = urllib.request.urlopen(url)
    response.read()

