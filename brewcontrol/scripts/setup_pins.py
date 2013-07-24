import sys

from pyramid.settings import aslist
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    # late import so we can run on a non-raspi device
    from RPi import GPIO

    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    GPIO.setmode(GPIO.BCM)
    for pin in map(int, aslist(settings["brewcontrol.inpins"])):
        GPIO.setup(pin, GPIO.IN)
    for pin in map(int, aslist(settings["brewcontrol.outpins"])):
        GPIO.setup(pin, GPIO.OUT)
