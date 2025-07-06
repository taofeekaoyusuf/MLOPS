import logging

# SETTING MULTIPLE LOGGERS FOR DIFFERENT OPERATIONS OF MODULES

# logger for Module 1
logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

# logger for Module 2
logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

# logger for Module 3
logger3 = logging.getLogger("module3")
logger3.setLevel(logging.ERROR)

# logger for Module 4
logger4 = logging.getLogger("module4")
logger4.setLevel(logging.INFO)

# logger for Module 5
logger5 = logging.getLogger("module5")
logger5.setLevel(logging.CRITICAL)

# Creating Logging Configuration
logging.basicConfig(
    filename='Python/loggers/logger.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

# ALTERNATIVELY
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    handlers=[
        logging.FileHandler('Python/loggers/logger.log'),
        logging.StreamHandler()
    ]
)