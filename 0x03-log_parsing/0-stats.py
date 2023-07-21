#!/usr/bin/python3

""" a log parsing script to get status code and number of
occurences when given input of the following format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>"""


import sys
from collections import Counter
import re
import signal

count = 0
pattern = r'\b(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b - \[(.*?)\] ' \
          r'"GET \/projects\/260 HTTP\/1\.1" \d+ \d+'
status = list()
file_size = 0


def keyboard_interrupt_handler(signal, frame):
    """A keyboard interrupt handler to handle ctrl + c"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)


def print_stats():
    """Prints all the statuses when needed"""
    output = Counter(status)
    print(f'File size: {file_size}')
    for stat, count in output.items():
        print(f"{stat}: {count}")


for line in sys.stdin:
    match = re.search(pattern, line.strip())
    if match:
        try:
            if count < 10:
                count += 1
                log = line.split(" ")
                status.append(log[7])
                file_size += int(log[8])
            else:
                print_stats()
                count = 0
        except KeyboardInterrupt:
            print_stats()
            sys.exit(0)
