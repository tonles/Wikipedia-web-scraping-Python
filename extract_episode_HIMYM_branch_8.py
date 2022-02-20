""""
Extracting n° of episodes from the given table
"""


def episodes_branch_8(soup, col, season_rows):
    table = soup.findAll('table', {'class': 'wikitable plainrowheaders wikiepisodetable'})[col]
    episodes_1 = []

    for row in table.findAll('tr')[
               1:]:  # We loop through all the table rows ('tr' tag), starting from row 1 (row 0 is the table's header)
        episode = row.findAll('th')[0]
        episodes_1.append(episode)

    # Extract and convert to int the episode numbers
    ep_new = []

    for index in range(season_rows):
        epi_1 = list(episodes_1[index])  # with list() I can extract data I need in the html page
        ep_new.append(epi_1)

    epi_list = [item for element in ep_new for item in element]  # convert a list of lists to a flat list
    del epi_list[11]
    episodes_1_int = [int(i) for i in epi_list]

    return episodes_1_int


