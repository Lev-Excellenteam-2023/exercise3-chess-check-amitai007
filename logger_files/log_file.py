import logging
import logging.config

# Set up logging configuration
logging.basicConfig(filename='game.log', level=logging.DEBUG,
                    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')

def logger():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')