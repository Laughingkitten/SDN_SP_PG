#coding:utf-8
import sys
#pip show nfcpyのLocationを記述する
sys.path.append('/home/ie_attend/.local/lib/python2.7/site-packages') 
import nfc
import threading
import traceback
import logging
import RPi.GPIO as GPIO
from time import sleep
from kafka import KafkaConsumer,KafkaProducer
from datetime import datetime as dt

idm = "default"
succes_idm = "default"

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT) # setup for LED1
GPIO.setup(26,GPIO.OUT) # setup for LED2
GPIO.setup(21,GPIO.OUT) #ブザーのsetup
p = GPIO.PWM(21,1)

def main(): 
    try:
        clf_IN = nfc.ContactlessFrontend('usb:001:005')
        clf_OUT = nfc.ContactlessFrontend('usb:001:007')

        GPIO.output(12,1)
        print GPIO.input(12)
        
        
        thread_attend = threading.Thread(target=func_attend,args=(clf_IN,))
        thread_leave = threading.Thread(target=func_leave,args=(clf_OUT,))

	thread_attend.start()
        thread_leave.start()
    except IOError:
        print 'deviceを認識できませんでした'
	#警告音を鳴らす(一応)
        buzzer()
        GPIO.output(12,0)
        sys.exit(88)
        
    except :
        #log_fmt = '%(asctime)s- %(message)'
        #logging.basicConfig(filename='attend_error.log',format=log_fmt)
        #logging.exception(err)
        traceback.print_exc()
        pass
        
def func_attend(clf_IN):
    while True:
        attend = clf_IN.connect(rdwr={'on-connect': connected})
        print ('attend-%s'% attend)
        print (idm)
        if (attend == True):
            GPIO.output(26,1)
            print "send_server"
            sleep(3)
            send_server(idm,1)
            GPIO.output(26,0)
            
def func_leave(clf_OUT):
    while True:
        leave = clf_OUT.connect(rdwr={'on-connect': connected})
        print ('leave-%s'%leave)
        print(idm)
        if (leave == True):
            GPIO.output(26,1)
            print "send_server"
            sleep(3)
            send_server(idm,0)
            GPIO.output(26,0)
            
def connected(tag):
    try:
	global succes_idm
        global idm
        line = str(tag).split()
        idm = line[4][3:19]
        #print idm
        if succes_idm != idm:
            succes_idm = idm
            return True
        else:
            print"used card"    
            return False
    except:
        #エラーを出力するだけ(プログラムは終了しない)
        traceback.print_exc()
        #e = open('error_log.txt','a')
        #e.write(traceback.print_exc())
        #e.write(dt.now())
        #e.close()
        return False

def send_server(idm,no):
    try:
	producer = KafkaProducer(bootstrap_servers='MQ_IPADDRESS')
        tdatetime = dt.now()
        strtime = tdatetime.strftime('%Y:%m:%d:%H:%M:%S')
        print idm
        print no
        idmetc = ('%s,ROOMID,%d'% (idm,no))
        merge = idmetc+","+str(strtime)
        producer.send('TOPIC_NAME',b'%s' % str(merge))
        producer.flush()
        producer.close()
        #送信完了音
	buzzer()        
        print "send complete"
        return
    except:
        traceback.print_exc()
        #e = open('error_log.txt','a')
        #e.write(traceback.print_exc())
        #e.write(dt.now())
        #e.close()
        return 

def buzzer():
    p.start(30)
    p.ChangeFrequency(262)
    sleep(0.5)
    p.ChangeFrequency(262)
    sleep(0.5)
    p.ChangeFrequency(392)
    sleep(0.5)
    p.ChangeFrequency(392)
    p.stop()
    return True

if __name__=="__main__":
    main()
