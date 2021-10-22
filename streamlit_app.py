from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Mr. Peach!

# Sample Input
        'area_home' : 140, #average area of livable space in germany
        'age_home' : 1960,
        'number_people' : 3,
        'age_windows' : 1980,
        'number_panes' : 1,
        'age_heating' : 1990,
        'old_type_heating' : 0, #oil heating
        'number_floor' : 2

# Sample output
        {'window': {'funding': 20, 'renovate': 1, 'cost': 12000, 'savings': 440}, 'heating': {'funding': '50', 'renovate': 1, 'cost': '15000', 'savings': '0'}}
"""

import requests

with st.form(key='my_form'):

    area_home = st.text_input("area_home")
    age_home = st.text_input("age_home")
    number_people = st.text_input("number_people")
    age_windows = st.text_input("age_windows")
    number_panes = st.text_input("number_panes")
    age_heating = st.text_input("age_heating")
    old_type_heating = st.text_input("old_type_heating")
    number_floor = st.text_input("number_floor")


    url = 'https://mrpeach-dot-interhyp-dps.ew.r.appspot.com'

    params = {'area_home' : 140, #average area of livable space in germany
            'age_home' : 1960,
            'number_people' : 3,
            'age_windows' : 1980,
            'number_panes' : 1,
            'age_heating' : 1990,
            'old_type_heating' : 0, #oil heating
            'number_floor' : 2
            }

    submit_button = st.form_submit_button(label='Submit parameters')

    if submit:
        response = requests.post(url, params)

