# coding:utf-8

# -----------------------------
# name : RYO Tsukayama
# aim : Pasori IC-card authenticate-system
# date : 2017/08/11
# -----------------------------







import sys
import os
sys.path.append(os.path.dirname(__file__) + '/nfcpy')
import nfc

#a number of user

#タッチされたときに実行する関数
def judge(tag):
    #print tag
    return tag


#USBカードリーダーと接続
clf = nfc.ContactlessFrontend('usb')

#恐らく、タッチされた時に呼び出す関数の設定
rdwr = {'on-connect':judge}

print 'Please tache your ID-card '
#clf.connectでPaSoRiを起動
clf.connect(rdwr=rdwr)
#print 'finish'


