#!/bin/python

import sqlite3
import time
import sys
import getopt

sensor_path='dummy_device'
frequency=10.0
db_path='temps.db'
simulator=False


def read_temp():
    if simulator: 
        return 4.0 #do something better here

    while True:
        sensor = open(sensor_path)
        output = sensor.readlines()
        sensor.close()
        if 'YES' in output[0]:
            return output[1].split('=')[1]
        else:
            time.sleep(1.0)    


def record_temp(c, temp):
    curtime = time.time()
    c.execute("INSERT INTO temps VALUES (%f, %s,100)" % (curtime, temp))

def recorder_loop(conn):
    c = conn.cursor()
    while True:
        temp = read_temp()
        record_temp(c, temp)
        conn.commit()
        time.sleep(frequency)

def main():
    global simulator
    try:
        opts, args = getopt.getopt(sys.argv[1:], "sd", [])
    except getopt.error, msg:
        print msg
        sys.exit(2)

    conn = sqlite3.connect(db_path)

    if "s" in opts: #simulator mode
        simulator=True
    if "d" in opts: #daemon mode
        recorder_loop(conn)
    else:  #oneshot mode
        c = conn.cursor()
        temp = read_temp()
        record_temp(c, temp)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
