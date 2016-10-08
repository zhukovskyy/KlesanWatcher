#!/usr/bin/bash

#set up your key for get wheater
#ref: http://opendata.cwb.gov.tw/usages
#export CWB_API=xxx-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

mkdir data

for i in {1..9}
do
	if [ `echo "$i % 2" | bc`  -eq  1 ]
	then
		wget "http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-00${i}&authorizationkey=${CWB_API}" -O "./data/F-D0047-00${i}"
	fi
done
for i in {10..87}
do
	if [ `echo "$i % 2" | bc`  -eq  1 ]
	then
		wget "http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-0${i}&authorizationkey=${CWB_API}" -O "./data/F-D0047-0${i}"
	fi
done
