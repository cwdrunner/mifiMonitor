#!/usr/bin/env python

# wifi.py

from splinter.browser import Browser
from time import sleep

URL = 'http://192.168.1.1/user_login.asp'
NAME = 'admin'
PASSWORD = '280dc932'


def main():
    br = Browser('firefox')
    br.visit(URL)
    sleep(3)
    if br.is_text_present('Password', wait_time=7):
        br.fill('userpass', PASSWORD)
        br.find_by_css('#LoginButton').first.click()
    sleep(3)
    if br.is_text_present('Connect', wait_time=7):
        br.find_by_id('#netmode_mode').first.click()
#############################################################################

if __name__ == "__main__":
    main()