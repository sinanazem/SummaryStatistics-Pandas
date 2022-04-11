import pandas as pd
from src.summary_statistics import summary_statistic





if __name__ == "__main__":


    # Summary Statistic for Marketing Campaign data
    house_price_df = pd.read_csv('src/data/house_price.csv')

    summary_statistic_house_price = summary_statistic(house_price_df)
    summary_statistic_house_price.to_csv('summary_statistic_house_price.csv')


    # Summary Statistic for Marketing Campaign data
    marketing_campaign_df = pd.read_csv('src/data/marketing_campaign.csv')

    summary_statistic_marketing_campaign = summary_statistic(house_price_df)
    summary_statistic_marketing_campaign.to_csv('summary_statistic_marketing_campaign.csv')


    print('Done!')





