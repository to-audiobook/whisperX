import contextlib;
import time;
import datetime;
@contextlib.contextmanager
def Time(prefix=""):
    '''log how long a block of code took to execute
    '''
    start = datetime.datetime.now();
    print(f'{start}: {prefix}...');
    try:
        yield
    finally:
        end = datetime.datetime.now();
        totalTime = end - start;
        print(f'{end}: {prefix} ran in {totalTime}');