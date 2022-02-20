""""
Main script for scraping data for "How I met your mother"
"""

import requests
from bs4 import BeautifulSoup
from extract_episode_HIMYM import episodes
from extract_episode_HIMYM_branch_7_9 import episodes_branch_7_9
from extract_episode_HIMYM_branch_8 import episodes_branch_8
from extract_viewers_HIMYM import viewers
from extract_viewers_HIMYM_branch_2 import viewers_branch_2
from extract_viewers_HIMYM_branch_3 import viewers_branch_3
from extract_dates_HIMYM import dates
import pandas as pd
import numpy as np

""""
Requesting data from the web
"""

url = 'https://en.wikipedia.org/wiki/List_of_How_I_Met_Your_Mother_episodes'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
total_episodes = []
total_viewers = []
total_dates = []


def main():
    """"
    Extracting data for Season 1 (rows in season's 1 table = 22)
    """
    episodes_1_int = episodes(soup, 0, 22)
    viewers_1_float = viewers(soup, 0, 22)
    air_dates_1 = dates(soup, 0, 22)

    total_episodes.append(episodes_1_int)
    total_viewers.append(viewers_1_float)
    total_dates.append(air_dates_1)

    """"
    Extracting data for Season 2 (rows in season's 2 table = 22)
    """

    episodes_2_int = episodes(soup, 1, 22)
    viewers_2_float = viewers_branch_2(soup, 1, 22)
    air_dates_2 = dates(soup, 1, 22)

    total_episodes.append(episodes_2_int)
    total_viewers.append(viewers_2_float)
    total_dates.append(air_dates_2)

    """"
    Extracting data for Season 3 (rows in season's 3 table = 20)
    """

    episodes_3_int = episodes(soup, 2, 20)
    viewers_3_float = viewers_branch_3(soup, 2, 20)
    air_dates_3 = dates(soup, 2, 20)

    total_episodes.append(episodes_3_int)
    total_viewers.append(viewers_3_float)
    total_dates.append(air_dates_3)

    """"
    Extracting data for Season 4 (rows in season's 4 table = 24)
    """

    episodes_4_int = episodes(soup, 3, 24)
    viewers_4_float = viewers(soup, 3, 24)
    air_dates_4 = dates(soup, 3, 24)

    total_episodes.append(episodes_4_int)
    total_viewers.append(viewers_4_float)
    total_dates.append(air_dates_4)

    """"
    Extracting data for Season 5 (rows in season's 5 table = 24)
    """

    episodes_5_int = episodes(soup, 4, 24)
    viewers_5_float = viewers(soup, 4, 24)
    air_dates_5 = dates(soup, 4, 24)

    total_episodes.append(episodes_5_int)
    total_viewers.append(viewers_5_float)
    total_dates.append(air_dates_5)

    """"
    Extracting data for Season 6 (rows in season's 6 table = 24)
    """

    episodes_6_int = episodes(soup, 5, 24)
    viewers_6_float = viewers(soup, 5, 24)
    air_dates_6 = dates(soup, 5, 24)

    total_episodes.append(episodes_6_int)
    total_viewers.append(viewers_6_float)
    total_dates.append(air_dates_6)

    """"
    Extracting data for Season 7 (rows in season's 7 table = 23)
    """

    episodes_7_int = episodes_branch_7_9(soup, 6, 23)
    viewers_7_float = viewers(soup, 6, 23)
    air_dates_7 = dates(soup, 6, 23)

    total_episodes.append(episodes_7_int)
    total_viewers.append(viewers_7_float)
    total_dates.append(air_dates_7)

    """"
    Extracting data for Season 8 (rows in season's 8 table = 23)
    """

    episodes_8_int = episodes_branch_8(soup, 7, 23)
    viewers_8_float = viewers(soup, 7, 23)
    air_dates_8 = dates(soup, 7, 23)

    total_episodes.append(episodes_8_int)
    total_viewers.append(viewers_8_float)
    total_dates.append(air_dates_8)

    """"
    Extracting data for Season 9 (rows in season's 9 table = 23)
    """

    episodes_9_int = episodes_branch_7_9(soup, 8, 23)
    viewers_9_float = viewers(soup, 8, 23)
    air_dates_9 = dates(soup, 8, 23)

    total_episodes.append(episodes_9_int)
    total_viewers.append(viewers_9_float)
    total_dates.append(air_dates_9)

    """"
    Working on the total lists
    """

    # Flatten each of the 3 lists
    total_episodes_flat = [item for element in total_episodes for item in element]
    total_viewers_flat = [item for element in total_viewers for item in element]
    total_dates_flat = [item for element in total_dates for item in element]

    total_episodes_array = np.array([total_episodes_flat])
    total_viewers_array = np.array([total_viewers_flat])
    total_dates_array = np.array([total_dates_flat])

    total_episodes_t = total_episodes_array.T
    total_viewers_t = total_viewers_array.T
    total_dates_t = total_dates_array.T

    # Arrange the new table into a data frame
    df_episodes = pd.DataFrame(total_episodes_t, columns=['Episode'])
    df_episodes.to_csv(r'C:\Users\Luca\PycharmProjects\pythonProject\tonle\Projects\BigBang\HIMYM_Scraping-episodes'
                       r'-results '
                       r'.csv', index=False)
    df_viewers = pd.DataFrame(total_viewers_t, columns=['Viewers (millions)'])
    df_viewers.to_csv(
        r'C:\Users\Luca\PycharmProjects\pythonProject\tonle\Projects\BigBang\HIMYM_Scraping-viewers-results.csv',
        index=False)
    df_dates = pd.DataFrame(total_dates_t, columns=['Air date'])
    df_dates['Air date'] = pd.to_datetime(df_dates['Air date'], format='%Y-%m-%d')
    df_dates.to_csv(
        r'C:\Users\Luca\PycharmProjects\pythonProject\tonle\Projects\BigBang\HIMYM_Scraping-dates-results.csv',
        index=False)

    pd.concat([df_episodes, df_viewers, df_dates], axis=1).to_csv(r'C:\Users\Luca\PycharmProjects\pythonProject\tonle'
                                                                  r'\Projects\BigBang\HIMYM_Scraping-results'r'.csv',
                                                                  index=False)


if __name__ == '__main__':
    main()
