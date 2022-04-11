import pandas as pd


def summary_statistic(df) -> pd.DataFrame:

        """
        function input: it get a pandas dataframe as a csv file
        output: return: retuen a information about columns as pandas dataframe

        """



        feature_describe = df.describe().T.reset_index().rename(
                               columns={'index':'feature'}).drop(columns='count')

        feature_info = pd.concat([df.dtypes,
                                   df.nunique(),
                                   df.isna().sum(),
                                   df.count()], axis=1,
                    keys=['type', 'count_unique', 'count_nan', 'count']).reset_index().rename(columns={'index':'feature'})

        summary_statistic_result = feature_info.merge(feature_describe, how='left', on='feature')

        return summary_statistic_result