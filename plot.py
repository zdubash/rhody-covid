import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plts

data_dimensions = {
    "Age_Cases" : [6, 19, [0, 4]],
    "Age_Hospitalizations" : [6, 19, [0, 6]],
    "Age_Deaths" : [6, 19, [0, 8]],
    "Race_Cases" : [21, 29, [0, 4]],
    "Race_Hospitalizations" : [21, 29, [0, 6]],
    "Race_Deaths" : [21, 29, [0, 8]],
}

graph_titles = {
    "Age_Cases" : ["Age Groups", "Percentage of Cases", "Percent of Rhode Island COVID Cases by Age"],
    "Age_Hospitalizations" : ["Age Groups", "Percent of Hospitalizations", "Percent of Rhode Island COVID Hospitalizations by Age"],
    "Age_Deaths" : ["Age Groups", "Percent of Deaths", "Percent of Rhode Island COVID Deaths by Age"],
    "Race_Cases" : ["Races", "Percent of Cases", "Percent of Rhode Island COVID Cases by Race"],
    "Race_Hospitalizations" : ["Races", "Percent of Hospitalizations", "Percent of Rhode Island COVID Hospitalizations by Race"],
    "Race_Deaths" : ["Races", "Percent of Deaths", "Percent of Rhode Island COVID Deaths by Race"],
}


def plot_demographic_data(qualifier):
    data = pd.read_csv("Demographics.csv")

    ddq = data_dimensions.get(qualifier)
    qualifier_data = data.iloc[ddq[0]:ddq[1], ddq[2]]

    qualifier_data.to_csv(qualifier + ".csv", header=[qualifier, "Percentage"], index = False)

    cleaned_qualifier_data = pd.read_csv(qualifier + ".csv")

    # Replace insignificant data with 0%.
    cleaned_qualifier_data["Percentage"] = cleaned_qualifier_data["Percentage"].replace("<1%", "0%")
    cleaned_qualifier_data["Percentage"] = cleaned_qualifier_data["Percentage"].replace("--", "0%")

    # Turn percentages into whole.
    cleaned_qualifier_data["Percentage"] = cleaned_qualifier_data["Percentage"].str[:-1].astype('int')

    # Convert columns to lists for easy graphing.
    qualifier_ranges = cleaned_qualifier_data[qualifier].to_list()
    percentage_ranges = cleaned_qualifier_data["Percentage"].to_list()

    # Initialize the graph
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(qualifier_ranges, percentage_ranges)
    ax.yaxis.set_major_formatter(plts.PercentFormatter(decimals = 0))

    # Assign axis labels and a title and then show the graph.
    plt.xlabel(graph_titles[qualifier][0])
    plt.ylabel(graph_titles[qualifier][1])
    plt.title(graph_titles[qualifier][2])
    plt.show()

def clean_heatmap_data(qualifier):
    # Assumes Municipality.csv has been downloaded. Ignores data after the 40 RI Municipalities.
    data = pd.read_csv("Municipality.csv", nrows=39)

    # print(data)

    # Cleans data for standardization.
    data["Municipality of residence"] = data["Municipality of residence"].str.lower()

    # Creates new CSV file containing only relevant data (Municipality names and per 100).
    data.iloc[:,[0,2]].to_csv("municipalities.csv", index = False) # 2 will change depending on what data needed.

