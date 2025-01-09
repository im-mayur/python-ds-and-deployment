import logging

logger1=logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2=logging.getLogger("module2")
logger2.setLevel(logging.CRITICAL)


logging.basicConfig(
    level=logging.CRITICAL,
    format="%(asctime)s-%(levelname)s:%(name)s:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)



## log message with different loggers
logger1.debug("This is debug message for module1")
logger2.warning("This is warning message for module2")
logger2.error("This is error message")
logger1.critical("This is criticl message for logger1")