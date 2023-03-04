import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)-12s %(levelname)s %(message)s",datefmt="%d-%m-%Y %H:%M:%S")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger




