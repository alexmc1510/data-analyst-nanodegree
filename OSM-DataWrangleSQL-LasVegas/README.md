# OpenStreetMap
Data Wrangling with SQL Project — Udacity Data Analyst Nanodegree

Name: Alejandro de la Mata
Map Area:  Las Vegas, Nevada

This project belongs to Udacity's [Data Analyst Nanodegree](https://eu.udacity.com/course/data-analyst-nanodegree--nd002).


## Technical Info
The project was built with:

* Python 2.7
* [NumPy](http://www.numpy.org/)
* SQL Database


## File Structure
The entire project is documented and explained in the 'OpenStreetMap.md' file.

Here's the file structure:

* `README.md`: this file
* `las-vegas_sample.osm`: sample data of the OSM file
* `audit.py`: audit street, city and update their names
* `data.py`: build CSV files from OSM and also parse, clean and shape data
* `database_create.py`: create database of the CSV files
* `query.py`: different queries about the database using SQL
* `OpenStreetMap.md`: REPORT
* `tags.py`: count multiple patterns in the tags
* `sample.py`: takes an `.osm` file as an input and outputs a k-reduced version of it. k is a parameter that can be changed in the code.
* `schema.py`: schema of how the data will be exported from the `.osm` file to the database.
* `mapparser.py`: uses iterative parsing to process the map file and find out how many of each tag there are.
