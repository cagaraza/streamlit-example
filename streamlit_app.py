from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Renovation 2500

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

    area_home = st.text_input("How many sqms does your house have?")
    age_home = st.text_input("What year was your house built/last fully renovated? (Year)")
    number_people = st.text_input("How many people live in your house?")
    age_windows = st.text_input("When were the windows installed (Enter year)")
    number_panes = st.text_input("How many panes does your windows have?")
    age_heating = st.text_input("When was the heating system installed?")
    old_type_heating = st.text_input("How is your house heated? (0 - oil, 1 - gas, 2 = pellet, 3 = brennwertkessel)")
    number_floor = st.text_input("How many stories does your house have?")

    submit_button = st.form_submit_button(label='Submit parameters')

    url = 'https://mrpeach-dot-interhyp-dps.ew.r.appspot.com'

    params = {'area_home' : area_home, 
            'age_home' : age_home,
            'number_people' : number_people,
            'age_windows' : age_windows,
            'number_panes' : number_panes,
            'age_heating' : age_heating,
            'old_type_heating' : old_type_heating, #oil heating
            'number_floor' : number_floor
            }

    if submit_button: 
        response = requests.post(url, params)

        for i in response.json().keys():
            st.write(i)
            st.write(response.json()[i])
