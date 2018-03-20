import os
import logging

from os.path import join

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

home_root = os.path.split(os.path.realpath(__file__))[0]

log_format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s' 
log_file = join(home_root, '../data/captcha-tensorflow.log')

logging.basicConfig(format=log_format, filename=log_file, level=logging.INFO)

formatter = logging.Formatter(log_format)

fileHandler = logging.FileHandler(log_file)
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

tfLogger = logging.getLogger('tensorflow')
tfLogger.setLevel(logging.ERROR)
tfLogger.addHandler(fileHandler)

