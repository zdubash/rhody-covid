# rhody-covid

This project is a library to perform simple analysis of COVID cases
in the state of Rhode Island. It is the second project in Olin's
[Software Design](https://softdes.olin.edu) course.

We retrieved all of our data from the [Rhode Island Department of Health](https://ri-department-of-health-covid-19-data-rihealth.hub.arcgis.com/).

The project contains a few files:
* Computational-Essay.ipynb -  The in depth analysis of our visualizations and functions.
* plot.py - The functions used to interact with and plot the data set.
* helpers.py - The functions used to download relevant data.
* test_plot.py - The functions used to test the data cleaning functions in `plot.py`.

In `helpers.py`, run `get_covid_data` or `get_all_covid_data` to download CSV files from the RIDOH Google Sheet. We recommend starting with `Demographics.csv` and `Municipality.csv`.

In `plot.py`, use `clean_demograhic_data` and `plot_demographic_data` as well as `clean_heatmap_data` and `plot_heatmap_data` to perform analysis and graphing of demographic and municipality data.

For the heatmaps to work properly, Geopandas and Descartes must be installed. Installation instructions are below.
Shapefiles for the state of Rhode Island are also necessary. Use `download_unzip` in `helpers.py` on this link to Rhode Island GIS files to obtain those: https://opendata.arcgis.com/datasets/957468e8bb3245e8b3321a7bf3b6d4aa_0.zip


Installed libraries are as follows:
* Geopandas: pip install geopandas
* Descartes: pip install descartes
