# U.S. Police Fatal Shootings Analysis (2015-2017)
This repository contains code and analysis for my capstone project on Police Fatal Shootings in the U.S. between the years 2015 and 2017. The goal of the project is to explore the nature of fatal police shootings across different U.S. states and races in order to find insights that could be helpful in reducing police brutality.

## Table of Contents
* Project Description
* Getting Started
  * Prerequisites
  * Installation
* Data
* Analysis

## Project Description
In this project, I analyzed police shooting data in the U.S. between 2015 and 2017. The analysis focused on identifying trends in shooting incidents across different states and races. Key questions answered include:
* Who were the victims?
* What were the circumstances?
* Was this a nation-wide problem? Or were some states and cities worse than others?

## Getting Started
### Prerequisites
This project requires Python 3.8+ and the following Python libraries installed:
* Numpy
* Pandas
* Matplotlib
* Seaborn
* Plotly
* GeoPy
* Joblib
* Statsmodels
* Scipy

### Installation
1. Clone this repository.
2. Install the prerequisites via pip:
```
pip install -r requirements.txt
```

### Data
The dataset used in this project contains information about police shootings in the U.S. between 2015 and 2017. Each row represents a separate incident, and the columns provide information such as the state where the shooting occurred, the race of the victim, whether the victim was armed, and the date of the incident.
The data used in this project was obtained from [https://www.kaggle.com/datasets/washingtonpost/police-shootings].

Additional data on U.S. demographics was collected from [https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-detail.html]. This dataset contains totals of U.S. demographics by state, gender, age, race and origin.

### Analysis
The analysis is contained in a Jupyter Notebook analysis.ipynb and includes:
Data Cleaning and Transformation
Exploratory Data Analysis
Statistical Analysis
Data Visualization

The custom functions used in the analysis are contained in the my_functions.py file.
