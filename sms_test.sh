#!/usr/bin/sh
if [ $# -eq 0 ]; then
    echo "USAGE: sms <phone_num ex: +886987026316> <ascii_txt ex: Test message>"
else
    echo "sending test sms to ${1}"
    echo "AT+CMGF=1\r" 
    echo -en "AT+CMGF=1\r" > /dev/ttyUSB0
    echo "AT+CSCA=\"+886935874443",145\r" 
    echo -en "AT+CSCA=\"+886935874443",145\r" > /dev/ttyUSB2
    echo "AT+CMGS=\"${1}\"\r" 
    echo -en "AT+CMGS=\"${1}\"\r" > /dev/ttyUSB0
    echo "${2}\032" 
    echo -en "${2}\032" > /dev/ttyUSB0
	cat /dev/ttyUSB0
fi
