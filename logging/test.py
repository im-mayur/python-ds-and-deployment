from logger import logging

def add(a,b):
    logging.debug("addition function is called")

    result =a+b
    return result

add(5,7)
logging.debug("addition is complete")