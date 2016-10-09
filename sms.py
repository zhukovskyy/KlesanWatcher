import subprocess
import logging


def send(phone_number, msg):
    logging.info('SMS to {}: {}'.format(phone_number, msg))
    result = subprocess.run(['./sms_test.sh', phone_number, msg])

    # TODO:the script is just POC, the status of sms are not handled, this need to refactor by python code
    if result.returncode:
        return "OK"
    else:
        logging.error('SMS to {} fail'.format(phone_number))
        return "Fail", 503

