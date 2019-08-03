import pandas as pd
from null_values_handler.null_values_handler import Null_values_Handler




def main():
    df_info = Null_values_Handler()
    df_info.report_null_values()
    df_info.handle_null_columns()
    # analysis.report_null_values()

if __name__ == '__main__':
    main()