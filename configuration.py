import pandas as pd
import numpy as np

FILE_PATH = 'D:/data/results.csv'
NULLS_THRESHOLD = 0.6
QUANTILES = [0.25,0.75]
AGG_FUNCS = ['min','median','mean','max','sum','std','var']

class Configuration:

    @staticmethod
    def get_csv_file_path():
        return FILE_PATH

    @staticmethod
    def get_agg_funcs():
        return AGG_FUNCS

    @staticmethod
    def get_quantiles():
        return QUANTILES

