import logging


class Logclass:
    def getlog(self):
        logger = logging.getLogger()

        # create handlers
        f_handler = logging.FileHandler('Log/myfile.log', mode='w')

        # create formatters and it to handlers
        f_format = logging.Formatter('%(asctime)s:%(levelname)s:%(module)s:%(message)s', datefmt='%d/%m/%Y')
        f_handler.setFormatter(f_format)

        # add handler to the logger
        logger.addHandler(f_handler)
        logger.setLevel(logging.DEBUG)

        return logger

        # logger.debug('This is a debug message')
        # logger.info('This is an info message')
        # logger.warning('This is a warning message')
        # logger.error('This is an error message')
        # logger.critical('This is a critical message')
