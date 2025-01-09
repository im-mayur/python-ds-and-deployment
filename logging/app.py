import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s:%(name)s:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def substract(a,b):
     result=a-b
     logger.debug(f"Substracting {a}-{b}={result}")
     return result

def multiply(a,b):
     result=a*b
     logger.debug(f"Multiplying {a}*{b}={result}")
     return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero")
        return None
    

add(10,20)
substract(77,32)
multiply(3,89)
divide(20,10)
