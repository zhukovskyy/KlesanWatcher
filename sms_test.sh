echo -en "AT+CMGF=1\r" > /dev/ttyUSB0
echo -en "AT+CMGS=\"+886987026316\"\r" > /dev/ttyUSB0
echo -en "test 天氣資訊\032" > /dev/ttyUSB0
