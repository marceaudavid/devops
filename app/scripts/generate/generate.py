import json
import random
import string
import time
from datetime import datetime

defaultunitnumber = 1


def unitnumber(number):
    if number <= 10:
        number = 1
        return number
    else:
        number += 1
        return number


def robottype():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))


def tanktemperature():
    return round(random.uniform(2.5, 4.1), 1)


def externaltemperature():
    return round(random.uniform(9, 14.1), 1)


def weightofmilkintank():
    return round(random.uniform(3512, 4607))


def generateaunit():
    data = {'robots': []}

    timestamp = time.time()
    timestamptostring = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')

    filename = str(unitnumber(defaultunitnumber)) + "-" + timestamptostring + ".json"

    for i in range(10):
        data['robots'].append({
            "Unit number": unitnumber(defaultunitnumber),
            "Robot number": i + 1,
            "Robot type": robottype(),
            "Tank temperature (Celsius)": tanktemperature(),
            "External temperature (Celsius)": externaltemperature(),
            "Weight of milk in tank (Kg)": weightofmilkintank(),
        })

        with open(filename, "w") as outfile:
            json.dump(data, outfile, indent=4)


generateaunit()
