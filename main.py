import pandas as pd
from null_values_handler.null_values_handler import Null_values_Handler
from descriptive_statistics_calculator.descriptive_statistics_calculator import Descriptive_Statistics_Calculator
from configuration import Configuration



def main():

    df = pd.read_csv(Configuration.get_csv_file_path())

    df_info = Null_values_Handler(df)
    df_info.report_null_values()
    # df_info.handle_null_columns()
    df_stats = Descriptive_Statistics_Calculator(df)
    df_stats.calculate_stats()
    # analysis.report_null_values()

if __name__ == '__main__':
    main()