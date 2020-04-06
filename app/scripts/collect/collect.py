import json
import random
import string


# Default value of unit number and robot number :
import time
from datetime import datetime

defaultunitnumber = 0
defaultrobotnumber = 0


def unitnumber(number):
    number += 1
    if number >= 5:
        number = 1
        return number
    else:
        return number


def robotnumber():
    return random.randrange(1, 11)


def robottype():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))


def tanktemperature():
    return round(random.uniform(2.5, 4.1), 1)


unitrobot = {
    "unitnumber": unitnumber(defaultunitnumber),
    "robotnumber": robotnumber(),
    "robottype": robottype(),
    "tanktemperature": tanktemperature()
}

unitrobotobject = json.dumps(unitrobot, indent=4)

timestamp = time.time()
timestamptostring = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
filename = str(unitnumber(defaultunitnumber)) + "-" + timestamptostring + ".json"
with open(filename, "w") as outfile:
    outfile.write(unitrobotobject)
