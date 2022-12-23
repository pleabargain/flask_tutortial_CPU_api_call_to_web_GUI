# use psutil 

import  psutil

def  get_cpu_percent():
    #include doc string
    """to get cpu percentage"""
    print( "CPU percent:" , psutil.cpu_percent(interval=    0.1), "%" )

def get_cpu_count():
    #include doc string
    """to get cpu count"""
    print( "CPU count:" , psutil.cpu_count()) 

get_cpu_percent()
get_cpu_count()