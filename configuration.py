import pandas as pd


FILE_PATH = 'D:/data/results.csv'
NULLS_THRESHOLD = 0.6

class Configuration:

    def get_raw_data_file(self):
        return 'D:/data/soccer/database.sqlite'

    def get_csv_file_path(self):
        return FILE_PATH
