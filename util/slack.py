import requests
from os import environ

_slack_api_key = environ.get('SLACK_API')


def log(msg):
    push('klesan_log', msg, 'logging')


def push(channel, msg, user):
    if not _slack_api_key:
        raise Exception('missing the slack token')

    requests.post('https://slack.com/api/chat.postMessage', data=dict(
        token=_slack_api_key,
        channel='#' + channel,
        username=user,
        text=msg
    ))

