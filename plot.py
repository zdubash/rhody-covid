"""
Library for cleaning and graphing Rhode Island COVID data

Authors: Zarius Dubash and Annie Sheil
"""

import pandas as pd
import geopandas as gpd

import matplotlib.pyplot as plt
import matplotlib.ticker as plts

# Dictionary that stores coordinate ranges of relevant data within
# Demographics.csv.
data_dimensions = {
    "Age_Cases": [6, 19, [0, 4]],
    "Age_Hospitalizations": [6, 19, [0, 6]],
    "Age_Deaths": [6, 19, [0, 8]],
    "Race_Cases": [21, 29, [0, 4]],
    "Race_Hospitalizations": [21, 29, [0, 6]],
    "Race_Deaths": [21, 29, [0, 8]],
}

# Dictionary that stores axis labels and graph titles.
graph_titles = {
    "Age_Cases": [
        "Age Groups",
        "Percentage of Cases",
        "Percent of Rhode Island COVID Cases by Age",
    ],
    "Age_Hospitalizations": [
        "Age Groups",
        "Percent of Hospitalizations",
        "Percent of Rhode Island COVID Hospitalizations by Age",
    ],
    "Age_Deaths": [
        "Age Groups",
        "Percent of Deaths",
        "Percent of Rhode Island COVID Deaths by Age",
    ],
    "Race_Cases": [
        "Races",
        "Percent of Cases",
        "Percent of Rhode Island COVID Cases by Race",
    ],
    "Race_Hospitalizations": [
        "Races",
        "Percent of Hospitalizations",
        "Percent of Rhode Island COVID Hospitalizations by Race",
    ],
    "Race_Deaths": [
        "Races",
        "Percent of Deaths",
        "Percent of Rhode Island COVID Deaths by Race",
    ],
}


def clean_demographic_data(qualifier):
    """
    Plot demographic data for the given qualifier.

    Arguments:
        qualifier: a String, representing one of the six dictionary keys in
        data_dimensions.

    Returns:
        a List of Lists representing qualifiers and percentages, ready for
        graphing.
    """

    data = pd.read_csv("Demographics.csv")

    # Get relevant qualifier data coordinates from dictionary,
    # assign data frame
    ddq = data_dimensions.get(qualifier)
    qualifier_data = data.iloc[ddq[0]: ddq[1], ddq[2]]

    # Write relevant qualifier data to new CSV file.
    qualifier_data.to_csv(
        qualifier + ".csv", header=[qualifier, "Percentage"], index=False
    )

    # Open recently created CSV file.
    Municipality_qualifier_data = pd.read_csv(qualifier + ".csv")

    # Replace insignificant data with 0%.
    Municipality_qualifier_data["Percentage"] = Municipality_qualifier_data[
        "Percentage"
    ].replace("<1%", "0%")
    Municipality_qualifier_data["Percentage"] = Municipality_qualifier_data[
        "Percentage"
    ].replace("--", "0%")

    # Turn percentages into whole.
    Municipality_qualifier_data["Percentage"] = (
        Municipality_qualifier_data["Percentage"].str[:-1].astype("int")
    )

    # Convert columns to lists for easy graphing.
    qualifier_ranges = Municipality_qualifier_data[qualifier].to_list()
    percentage_ranges = Municipality_qualifier_data["Percentage"].to_list()

    return [qualifier_ranges, percentage_ranges]


def plot_demographic_data(qualifier, ranges):
    """
    Plot demographic data for the given qualifier.

    Arguments:
        qualifier: a String, representing one of the six dictionary keys in
            data_dimensions.
        ranges: a List of Lists, containing a list of data for each axis in
            the graph.
    """

    # Initialize the graph
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(ranges[0], ranges[1])
    ax.yaxis.set_major_formatter(plts.PercentFormatter(decimals=0))

    # Assign axis labels and a title and then show the graph.
    plt.xlabel(graph_titles[qualifier][0])
    plt.xticks(rotation=90, horizontalalignment="left")
    plt.ylabel(graph_titles[qualifier][1])
    plt.title(graph_titles[qualifier][2])
    plt.show()


heatmap_data_dimensions = {
    "Cases": [2, "Rate of COVID-19 cases per 100,000 population", 10000],
    "Hospitalizations": [4,
                         "Rate of hospitalizations per 100,000 population",
                         700],
    "Deaths": [6, "Rate of deaths per 100,000 population", 400],
}


def clean_heatmap_data(qualifier):
    """
    Clean Municipality data for use in heatmap.

    Arguments:
        qualifier: a String, representing one of the three dictionary keys in
        heatmap_data_dimensions.
    """

    # Assumes Municipality.csv has been downloaded. Ignores data after the 40
    # RI Municipalities.
    data = pd.read_csv("Municipality.csv", nrows=39)

    # Cleans data for standardization.
    data["Municipality of residence"
         ] = data["Municipality of residence"].str.lower()
    data[heatmap_data_dimensions[qualifier][1]] = data[
        heatmap_data_dimensions[qualifier][1]
    ].replace("--", "0")

    # Creates new CSV file containing only relevant data
    # (Municipality names and per 100).
    data.iloc[:, [0, heatmap_data_dimensions[qualifier][0]]].to_csv(
        "Municipality_" + qualifier + ".csv", index=False
    )  # 2 will change depending on what data needed.


def plot_heatmap_data(qualifier):
    """
    Generate a heat map with given data.

    Arguments:
        qualifier: a String, representing one of the three dictionary keys in
        heatmap_data_dimensions.
    """

    data = pd.read_csv("Municipality_" + qualifier + ".csv")

    nb = "Municipalities__1997_.shp"  # Shapefile downloaded in notebook
    regions = gpd.read_file(nb)
    regions["Municipalities"] = regions["NAME"].str.lower()

    merged = regions.set_index("Municipalities").join(
        data.set_index("Municipality of residence")
    )
    merged = merged.reset_index()
    merged = merged.fillna(0)

    fig, ax = plt.subplots(1, figsize=(20, 10))
    ax.axis("off")
    ax.set_title(
        heatmap_data_dimensions[qualifier][1],
        fontdict={"fontsize": "20", "fontweight": "3"},
    )
    color = "Oranges"
    vmin = 0
    # Set scale max to predefined number listed in above dictionary
    vmax = heatmap_data_dimensions[qualifier][2]
    sm = plt.cm.ScalarMappable(cmap=color,
                               norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    cbar = fig.colorbar(sm)
    cbar.ax.tick_params(labelsize=10)
    merged.plot(
        heatmap_data_dimensions[qualifier][1],
        cmap=color,
        linewidth=0.8,
        ax=ax,
        edgecolor="0.8",
        figsize=(20, 10),
    )
    plt.show()
