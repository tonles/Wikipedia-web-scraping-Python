""""
Extracting air dates from the given table
"""
from datetime import datetime
import string


def dates(soup, col, season_rows):
    # Extract and convert to date the date of first airing
    table = soup.findAll('table', {'class': 'wikitable plainrowheaders wikiepisodetable'})[col]
    air_dates_1 = []
    for row in table.findAll('tr')[1:]:
        air_date = row.findAll('td')[4]
        test_2 = air_date.findAll(text=True)
        test_3 = ''.join(p.strip(string.whitespace + '"') for p in test_2[:-3])  # Extract date from HTML
        test_4 = test_3.replace(u'\xa0', u'')
        air_dates_1.append(test_4)

    air_dates_1_final = []
    for index in range(season_rows):
        air_1 = air_dates_1[index]
        air_2 = datetime.strptime(air_1, '%B%d,%Y')
        air_3 = str(datetime.date(air_2))
        air_dates_1_final.append(air_3)

    return air_dates_1_final
