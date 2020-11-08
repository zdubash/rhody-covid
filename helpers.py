"""
Library for programmatically downloading Rhode Island COVID data
from Google Sheets

Authors: Zarius Dubash and Annie Sheil
"""

import pandas as pd
import requests
import matplotlib.pyplot as plt

# Data GIDs
data_gids = {
    "Summary": "264100583",
    "Trends": "1592746937",
    "Demographics": "31350783",
    "Case Trends by Age": "1972249663",
    "Rate Trends by Age": "1199034078",
    "Case Trends by Race": "1074078949",
    "Rate Trends by Race": "2131764372",
    "Municipality": "901548302",
    "Municipal Case Trends": "789241605",
    "Municipal Rate Trends": "2009233256",
    "Municipal Test Trends": "1009795789",
    "Municipal Percent Positive Trends": "351133654",
    "Cases by ZCTA": "365656702",
    "Cumulative Long Term Care and Assisted Living": "500394186",
}

# Sorry this line is over 80 characters.
covid_data_csv_url = "https://docs.google.com/spreadsheets/d/1c2QrNMz8pIbYEKzMJL7Uh2dtThOJa2j1sSMwiDo5Gz4/export?format=csv&id=1c2QrNMz8pIbYEKzMJL7Uh2dtThOJa2j1sSMwiDo5Gz4&gid="


def get_covid_data(worksheet):
    """
    Gets data from the web and opens in a CSV file.

    This function uses the given URL that hosts the Google Sheets containing
    all the Rhode Island COVID data from the Department of Health.

    Arguments:
        worksheet: A String that is the specific worksheet being requested
        from the workbook.
    """

    csv_url = covid_data_csv_url + data_gids[worksheet]
    res = requests.get(url=csv_url)
    open(worksheet + ".csv", "wb").write(res.content)


def get_all_covid_data():
    """
    Opens every individual sheet within the Rhode Island COVID data Google
    Sheet and writes the data to CSV files.
    """

    for worksheet in data_gids:
        get_covid_data(worksheet)


def download_unzip(url):
    """
    Given the path to a ZIP file, downloads and unzips the contents.

    Arguments:
    url: A string that is the URL at which the ZIP file is located.
    """

    import zipfile
    import io

    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
