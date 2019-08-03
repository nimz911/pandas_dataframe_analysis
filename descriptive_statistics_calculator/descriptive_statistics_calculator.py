import pandas as pd
from collections import  defaultdict

from configuration import Configuration


class Descriptive_Statistics_Calculator:
    def __init__(self, data_frame):
        # type: (pd.DataFrame) -> None

        self.data_frame = data_frame
        self.config = Configuration()


    def calculate_stats(self):
        stats = defaultdict(lambda: defaultdict(dict))
        for col in self.data_frame.columns:
            if (str(self.data_frame[col].dtype).__contains__('int')) | (str(self.data_frame[col].dtype).__contains__('float')):
                for agg_func in self.config.get_agg_funcs():
                    stats[col][agg_func] = round(self.data_frame[col].agg(agg_func),4)
                    for quantile in self.config.get_quantiles():
                        stats[col]['quantile_'+str(quantile)] =self.data_frame[col].quantile(quantile)

        stats_df = pd.DataFrame(stats)

        print(stats_df)
        return stats_df
