from logger import logger1, logger2, logger3, logger4, logger5, logging

def add(a, b):
    logging.debug("Addition operation is taking place, be warned")
    return a+b


logging.debug("Call to Addition function is being made")
add(8,7)

logger1.debug("This is an error message for Module 1")

logger2.warning("This is an info message for Module 2")

logger3.error("This is a error message log for Module 3")

logger4.info("This is a info message for Module 4")

logger5.critical("This is an critical message for Module 5")