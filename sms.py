import subprocess
import logging


def send(phone_number, msg):
    logging.info('SMS to {}: {}'.format(phone_number, msg))
    return_code = subprocess.run(['./sms_test.sh', phone_number, msg])
    if return_code:
        logging.error('SMS to {} fail'.format(phone_number))

