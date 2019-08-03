
import pandas as pd
from configuration import Configuration

class Fill_NA_Methods:
    FFILLE = 'ffill'

class Null_values_Handler:
    def __init__(self, data_frame):
        # type: (pd.DataFrame) -> None

        self.config = Configuration()
        self.data_frame = data_frame


    def handle_null_columns(self, null_threshold=0.5, fill_method=Fill_NA_Methods.FFILLE):
        na_percentage = self.data_frame.isna().sum() / self.data_frame.shape[0]

        for col in self.data_frame.columns:
            col_null_percentage = round(na_percentage[na_percentage.index == col][0],4)
            if col_null_percentage > null_threshold:
                self.data_frame.drop(col, 1, inplace=True)
                print(self.__report_removed_column(col, col_null_percentage))
            elif col_null_percentage == 0:
                continue
            else:
                self.data_frame[col].fillna(method=fill_method)
                print(self.__report_filled_column(col, col_null_percentage))


    def report_null_values(self):
        absolute_values = pd.DataFrame(self.data_frame.isna().sum())
        absolute_values.rename(columns={0: 'null_count'}, inplace=True)
        percentage = pd.DataFrame(self.data_frame.isna().sum() / self.data_frame.shape[0])
        percentage.rename(columns={0: 'null_percent'}, inplace=True)

        null_info = absolute_values.join(percentage)
        print(null_info)

        return null_info


    def __read_data_frame_from_csv(self):
        return pd.read_csv(self.config.get_csv_file_path())



    @staticmethod
    def __report_removed_column(column, column_null_percentage):
        return 'column {} contains {}% of null values - column removed'.format(column, column_null_percentage)

    @staticmethod
    def __report_filled_column(column, column_null_percentage):
        return 'column {} contains {}% of null values - apply fillna with ffill method'.format(column, column_null_percentage)


