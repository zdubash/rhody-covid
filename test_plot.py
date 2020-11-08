"""
Library to test plot.py data cleaning functions.

Authors: Zarius Dubash and Annie Sheil
"""

import plot

test_dimensions = {
    "Age_Cases": [
        [
            "0-4",
            "5-9",
            "10-14",
            "15-18",
            "19-24",
            "25-29",
            "30-39",
            "40-49",
            "50-59",
            "60-69",
            "70-79",
            "80-89",
            "90+",
        ],
        [2, 2, 2, 4, 12, 9, 16, 14, 14, 10, 6, 5, 3],
    ],
    "Age_Hospitalizations": [
        [
            "0-4",
            "5-9",
            "10-14",
            "15-18",
            "19-24",
            "25-29",
            "30-39",
            "40-49",
            "50-59",
            "60-69",
            "70-79",
            "80-89",
            "90+",
        ],
        [1, 0, 0, 1, 3, 3, 7, 11, 15, 19, 19, 13, 6],
    ],
    "Age_Deaths": [
        [
            "0-4",
            "5-9",
            "10-14",
            "15-18",
            "19-24",
            "25-29",
            "30-39",
            "40-49",
            "50-59",
            "60-69",
            "70-79",
            "80-89",
            "90+",
        ],
        [0, 0, 0, 0, 0, 0, 1, 1, 4, 11, 23, 32, 27],
    ],
    "Race_Cases": [
        [
            "Hispanic or Latino†",
            "American Indian or Alaska Native*",
            "Asian*",
            "Black or African American*",
            "Native Hawaiian or Other Pacific Islander*",
            "White*",
            "Other race*",
            "Multiple race*",
        ],
        [43, 0, 2, 11, 0, 42, 2, 1],
    ],
    "Race_Hospitalizations": [
        [
            "Hispanic or Latino†",
            "American Indian or Alaska Native*",
            "Asian*",
            "Black or African American*",
            "Native Hawaiian or Other Pacific Islander*",
            "White*",
            "Other race*",
            "Multiple race*",
        ],
        [36, 0, 2, 12, 0, 47, 2, 0],
    ],
    "Race_Deaths": [
        [
            "Hispanic or Latino†",
            "American Indian or Alaska Native*",
            "Asian*",
            "Black or African American*",
            "Native Hawaiian or Other Pacific Islander*",
            "White*",
            "Other race*",
            "Multiple race*",
        ],
        [11, 0, 1, 6, 0, 81, 0, 0],
    ],
}


def test_clean_demographic_data():
    for item in plot.data_dimensions:
        assert plot.clean_demographic_data(item) == test_dimensions[item]


heatmap_test_dimensions = ["Cases", "Hospitalizations", "Deaths"]


def test_clean_heatmap_data():
    import os.path
    from os import path

    for item in plot.heatmap_data_dimensions:
        plot.clean_heatmap_data(item)
    for dimension in heatmap_test_dimensions:
        assert path.exists("Municipality_" + dimension + ".csv")
