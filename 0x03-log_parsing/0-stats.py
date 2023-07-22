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
file_size = 0


def keyboard_interrupt_handler(signal, frame):
    """A keyboard interrupt handler to handle ctrl + c"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)


def print_stats():
    """Prints all the statuses when needed"""
    if file_size > 0:
        print(f'File size: {file_size}')
    for stat, count in sorted(statuses.items()):
        if count > 0:
            print(f'{stat}: {count}')


statuses = {
        '200': 0,
        '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}


for line in sys.stdin:
    match = re.search(pattern, line.strip())
    if match:
        try:
            count += 1
            log = line.split()
            if log[7] in statuses:
                statuses[log[7]] += 1
                file_size += int(log[8])
            if count == 10:
                print_stats()
                count = 0
        except KeyboardInterrupt:
            print_stats()
            sys.exit(0)
        except TypeError:
            continue
