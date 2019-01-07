#!/usr/bin/env python

# monitor_wifi.py

import os
import psutil
from jabbapylib.network import network
from time import sleep
from datetime import datetime
from jabbapylib.process import process

PROCNAME = 'firefoxdriver'
SLEEP_TIME = 1 * 60


def kill_firefoxdriver():
    print '# killing firefoxdriver'
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            proc.kill()


def start_wifi():
    print '# restarting wifi ({now})'.format(now=datetime.now())
    #   os.chdir('/home/jabba/bin.python')
    process.execute_cmd_in_background("./wifi.py")


def main():
    while True:
        if not network.is_internet_on():
            print '# network is down'
            kill_firefoxdriver()
            start_wifi()
            kill_firefoxdriver()
        else:
            print '# network is up'
            pass

        print '# sleeping...'
        sleep(SLEEP_TIME)


#############################################################################

if __name__ == "__main__":
    main()