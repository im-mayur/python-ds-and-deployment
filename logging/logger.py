import logging


## Configure basic Configuration 

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format="%(asctime)s-%(levelname)s:%(name)s:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    )