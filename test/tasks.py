
import time
import datetime

from greenGiant.celeryApp import app


@app.task
def add(x, y):
    time.sleep(10)
    print("{} + {} = {}".format(x, y, x+y))
    return x + y


@app.task
def print_datetime():
    print(datetime.datetime.now().strftime("%Y%m%d %H%M%S"))
