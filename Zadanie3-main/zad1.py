import logging

def get_logs(level, format_string):
    logging.basicConfig(level=level, format=format_string)
    return logging

logger = get_logs(logging.DEBUG, '%(asctime)s - %(levelname)s - %(message)s')
logger.debug("Debugujesz")
logger.info("Informacja = Wygrałeś")
logger.error("błąd")
logger.warning("Uwaga !!!!")
logger.critical("Sytuacja krytyczna")
logger.notset("nie ustawiony")
