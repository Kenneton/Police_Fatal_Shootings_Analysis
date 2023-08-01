import pandas as pd
import time
import typing

import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim


def millions_formatter(x: float, pos=None, decimals: int = 0) -> str:
    """The two args are the value and tick position"""
    format_string = "{:." + str(decimals) + "f}M"
    return format_string.format(x * 1e-6)


def plot_barchart(df: pd.DataFrame, order: bool = False, percent: bool = True) -> None:
    """
    Plots a barchart with low ink-to-data ratio from a dataframe.
    Annotates the values and percentages (optional).
    Automatically converts large values to millions.
    """

    if order == True:
        df = df.sort_values(by=df.columns[1], ascending=False)

    g = sns.barplot(data=df, x=df.columns[0], y=df.columns[1], color="grey", width=0.7)
    if percent == True:
        total = df[df.columns[1]].sum()
        for index, value in enumerate(df[df.columns[1]]):
            percentage = "{:.1f}%".format(100 * value / total)

            if value > 1e5:
                plt.text(
                    index,
                    value,
                    f"{millions_formatter(value, decimals=1)}\n({percentage})",
                    horizontalalignment="center",
                    verticalalignment="bottom",
                    color="black",
                )

            else:
                plt.text(
                    index,
                    value,
                    f"{int(value)}\n({percentage})",
                    horizontalalignment="center",
                    verticalalignment="bottom",
                    color="black",
                )

    else:
        for index, value in enumerate(df[df.columns[1]]):
            if value > 1e5:
                plt.text(
                    index,
                    value,
                    millions_formatter(value, decimals=1),
                    horizontalalignment="center",
                    verticalalignment="bottom",
                    color="black",
                )
            else:
                plt.text(
                    index,
                    value,
                    str(value),
                    horizontalalignment="center",
                    verticalalignment="bottom",
                    color="black",
                )

    sns.despine(left=True, bottom=True)
    plt.yticks([])
    g.set_xlabel("")
    g.set_ylabel("")


def get_city_location(cities):
    """
    Function for getting USA city locations from their name, and saving them to a file.
    Warning: can take a long time to run (>20min).
    """
    geolocator = Nominatim(user_agent="cities_mapping_USA_123")

    latitude = []
    longitude = []
    for city in cities["City"]:
        location = geolocator.geocode(city)
        if location:
            latitude.append(location.latitude)
            longitude.append(location.longitude)
        else:
            latitude.append(None)
            longitude.append(None)
        time.sleep(1)

    cities["latitude"] = latitude
    cities["longitude"] = longitude

    cities.to_csv("city_locations.csv", index=False)
    return cities


def format_state_name(
    df: pd.DataFrame, column_name: str, to_acronym: bool = True
) -> pd.DataFrame:
    """Changes state name to acronymn, and vice versa."""

    state_to_acronym = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
    }

    acronym_to_state = {v: k for k, v in state_to_acronym.items()}

    if to_acronym is True:
        df[column_name] = df[column_name].replace(state_to_acronym)

    # changes back to full state name
    elif to_acronym is False:
        df[column_name] = df[column_name].replace(acronym_to_state)

    return df
