import urllib.request
import os

import pytest
import slack


def test_log_to_slack():
    slack.log('log to slack test')


