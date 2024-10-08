# SPDX-FileCopyrightText: 2022 Scott Shawcroft for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Tests NTP with CPython socket"""

import socket
import time

import adafruit_ntp

ntp = adafruit_ntp.NTP(socket, cache_seconds=3600)

while True:
    print(ntp.datetime)
    time.sleep(1)
