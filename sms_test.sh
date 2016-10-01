#!/usr/bin/sh
if [ $# -eq 0 ]; then
    echo "USAGE: sms <phone_num ex: +886987026316> <ascii_txt ex: Test message>"
else
    echo "sending test sms to ${1}"
    echo -en "AT+CMGF=1\r" > /dev/ttyUSB2
    #echo -en "AT+CSCA=\"${SMS_SERVICE_NUMBER}\",145\r" > /dev/ttyUSB2
    echo -en "AT+CMGS=\"${1}\"\r" > /dev/ttyUSB2
    echo -en "${2}\032" > /dev/ttyUSB2
fi
