from jobs import rq

from random import randint
from time import sleep


@rq.job
def sample_job1():
    sleep(randint(1, 10))

    # Chance of failing
    if randint(1, 100) < 10:
        raise Exception("Fail!")


@rq.job
def sample_job2():
    sleep(randint(10,100))

