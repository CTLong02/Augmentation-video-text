import os
import logging

import numpy as np
from torch.utils.tensorboard import SummaryWriter


def validate_log_path(log_path):
    if log_path is None:
        print('log_path is empty')
        return False
    if os.path.exists(log_path):
        if not os.access(log_path, os.W_OK):
            print(f'Cannot write to the directory: {log_path}')
            return False
        print(f'{log_path} already exists.')
        return False
    os.makedirs(log_path, exist_ok=True)
    return True


def set_logger(log_path, log_name='training'):
    if log_path is None:
        print('log_path is empty')
        return None

    if os.path.exists(log_path):
        print('%s already exists' % log_path)
        return None

    logger = SummaryWriter(log_dir=log_path)
    return logger


def __set_logger(log_path, log_name='training'):
    if log_path is None:
        print('log_path is empty')
        return None

    if os.path.exists(log_path):
        print('%s already exists' % log_path)
        return None

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    logfile = logging.FileHandler(log_path)
    console = logging.StreamHandler()
    logfile.setLevel(logging.INFO)
    logfile.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(logfile)
    logger.addHandler(console)

    return logger
