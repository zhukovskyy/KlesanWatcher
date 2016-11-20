from nameko.timer import timer
from datetime import datetime
import logging

from util.location_parser import update_weather_from_data_id


class RegularJobs(object):
    name = "regular_job"

    @timer(interval=10)
    def jobs(self):
        now = datetime.now()
        if not now.hour % 3 and not now.minute and now.second < 10:
            self.update_weather()

        self.update_sms_msg()
        self.send_weather()

    def update_weather(self):
        """update the weather from cwb
        """
        logging.info('Updating weather from CWB')
        with open('cwb_data_id.txt', 'r') as f:
            for line in f:
                data_id = line.strip()
                update_weather_from_data_id(data_id)

    def update_sms_msg(self):
        """geting the sms msg"""
        logging.debug('read sms msgs..')

    def send_weather(self):
        logging.debug('send sms weather msgs..')
