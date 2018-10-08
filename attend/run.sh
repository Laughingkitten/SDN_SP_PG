#!/bin/bash

TEST=(`lsusb | grep 054c:06c3 | sed s/"Bus 001 Device "//g | sed s/": ID 054c:06c3 Sony Corp.//g"`)
echo ${TEST[0]}
echo ${TEST[1]}

TEST2=`sudo udevadm info -q all -n /dev/bus/usb/001/${TEST[0]} | grep ID_SERIAL_SHORT`
TEST2=`echo "$TEST2" | sed s/"E: ID_SERIAL_SHORT="//g`
echo $TEST2


TEST3=`sudo udevadm info -q all -n /dev/bus/usb/001/${TEST[1]} | grep ID_SERIAL_SHORT`
TEST3=`echo "$TEST3" | sed s/"E: ID_SERIAL_SHORT="//g`
echo $TEST3

if [ $TEST2 == "0523814" ];
then
	echo "INは${TEST[0]}"
	echo "OUTは${TEST[1]}"
	sed -e "s/"OUT_PASORI"/${TEST[1]}/g" -e "s/"IN_PASORI"/${TEST[0]}/g" test_attend.py > ie_attend.py
	sudo python ie_attend.py
	RET=$?
	echo $RET #[$?]は直前のコマンドからの返り値
	if [ $RET -eq 88 ]; then
	    sudo reboot
	    #exit 1
	elif [ $RET -ne 0 ]; then
	    #sudo python ie_attend.py
	    exit 1
	else
	    : 
	fi
	
else
	echo "INは${TEST[1]}"
	echo "OUTは${TEST[0]}"
	sed -e "s/"OUT_PASORI"/${TEST[0]}/g" -e "s/"IN_PASORI"/${TEST[1]}/g" test_attend.py > ie_attend.py
        sudo python ie_attend.py
	RET=$?
	echo $RET
	if [ $RET -eq 2 ]; then
	    sudo reboot
	    #exit 1
	elif [ $RET -ne 0 ]; then
	    #sudo python ie_attend.py
	    exit 1
	else
	    :
	fi
		
	
fi
