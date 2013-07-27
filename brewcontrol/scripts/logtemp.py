#!/usr/bin/env python

import os
import sys
import transaction
from datetime import datetime
from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    TempSample,
    )

import time
from argparse import ArgumentParser
from brewcontrol.sensors import read_temp

DEMO_MODE=True

DEMO_PATH='dummy_device'

def record_temp(c, temp):
    curtime = time.time()
    c.execute("INSERT INTO temps VALUES (%f, %s,100)" % (curtime, temp))

def parse_args():
    p = ArgumentParser()
    p.add_argument('config')
    p.add_argument('-D', '--demo-mode', action='store_true')
    return p.parse_args()

def main():
    args = parse_args()
    setup_logging(args.config)
    settings = get_appsettings(args.config)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    if args.demo_mode:
        sensors = [DEMO_PATH]
    else:
        base = "/sys/bus/w1/devices/"
        sensors = os.listdir(base)

    if not sensors:
        raise RuntimeError("Can't find any temperature sensor.  Did you"
                           " modprod the w1 modules?")

    with transaction.manager:
        for s in sensors:
            try:
                sensor_path(s)
            except ValueError:
                # probably not a valid sensor
                continue
            temp = read_temp(s)
            rec = TempSample(datetime.now(), s, temp, 65)
            DBSession.add(rec)


if __name__ == "__main__":
    main()
