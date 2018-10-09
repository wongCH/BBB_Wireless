#!/usr/bin/python3
import os
import sys

from Helpers.Constant import *
from datetime import datetime
from pathlib import Path

class Logging(object):
    """ Logging and appending data to log file

    Each record contains 2000 consecutive readings at 5ms interval.

    After 2000 readings, data will be compressed and published to mqtt

    and save to data base
    ---------------------------------------------------------------
    "x" - Create - will create a file, returns an error if the file exist
    "a" - Append - will create a file if the specified file does not exist
    "w" - Write - will create a file if the specified file does not exist
    """  
  
    def Save(self,content):
        

        if not os.path.exists(os.path.dirname(Constant.FILE_STORE_NAME)):
            try:
                os.makedirs(os.path.dirname(Constant.FILE_STORE_NAME))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(Constant.FILE_STORE_NAME, "a") as f:
            f.write(content)
            f.writelines("\n")