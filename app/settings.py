import logging

class mylogger(logging.Logger):

    def __init__(self, name, level=logging.DEBUG):
        super().__init__(name, level=level)



    def log_with_prefix(self, prefix, msg, *args, **kwargs):
        self.log(logging.INFO, f"{prefix} - {msg}", *args, **kwargs)


    def log_error(self, msg, *args, **kwargs):
        handler = logging.FileHandler('logs/custom_errors.logs')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        handler.mode = 'a'
        self.addHandler(handler)
        self.log_with_prefix("ERROR", msg, *args, **kwargs)


    def middleware_log(self, msg, *args, **kwargs):
        handler = logging.FileHandler('logs/api_calls.logs')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        handler.mode = 'a'
        self.addHandler(handler)
        self.log_with_prefix("MIDDLEWARE", msg, *args, **kwargs)


    def custom_log(self, msg, *args, **kwargs):
        handler = logging.FileHandler('logs/custom_logs.logs')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        handler.mode = 'a'
        self.addHandler(handler)
        self.log_with_prefix("CUSTOM", msg, *args, **kwargs)

logger = mylogger(__name__)



# usage example
# from app.settings import mylogger

# logger = mylogger(__name__)

# logger.debug("get all verticals")
# logger.info("get all verticals")
# logger.error("get all verticals")
# logger.log_error("get all verticals")
# logger.logs(logging.INFO, "This is a regular logs message")
# logger.log_with_prefix("DEBUG", "This is a debug message")





