""""
Extracting n° of viewers from the given table
"""


def viewers(soup, col, season_rows):
    table = soup.findAll('table', {'class': 'wikitable plainrowheaders wikiepisodetable'})[col]
    viewers_1 = []

    for row in table.findAll('tr')[
               1:]:  # We loop through all the table rows ('tr' tag), starting from row 1 (row 0 is the table's header)
        viewer = row.findAll('td')[6]  # For all table rows with 'td' tag (table data), we grab only data from
        # position 6, that is n° of viewers
        viewers_1.append(viewer)

    # Extract and convert to float the number of viewers
    vie_new = []
    for index in range(season_rows):
        vie_2 = list(viewers_1[index])
        vie_new.append(vie_2)

    vie_list = [item for element in vie_new for item in element]
    vie_list_2 = []
    for i in range(0, len(vie_list)):  # Take only the odd elements of the list "vie_list"
        if i % 2:
            continue
        else:
            vie_list_2.append(vie_list[i])

    viewers_1_float = [float(i) for i in vie_list_2]

    return viewers_1_float
