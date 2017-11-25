#!/usr/bin/env python
# coding:utf-8
import subprocess
import sys
import Get_idm


def callback_method(query):
    return ['Hello', 'World!', 'with', query]

def exe_scan():
    try:
        cmd='sudo python /home/pi/httpserver/test.py'
        res = subprocess.check_output(cmd.split(" "))
        #print(res)
    except:
        print ("Error.")
        #print(res)
    return res
    


if __name__ == '__main__':
    port = sys.argv[1]
    Get_idm.start(port, exe_scan())

