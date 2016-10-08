from nameko.timer import timer


class RegularJobs(object):
    name = "regular_job"

    @timer(interval=10)
    def jobs(self):
        self.update_weather()
        self.update_sms_msg()
        self.send_weather()

    def update_weather(self):
        """update the weather from cwb
        """
        print('updating..')

    def update_sms_msg(self):
        print('read sms msgs..')

    def send_weather(self):
        print('send sms weather msgs..')
