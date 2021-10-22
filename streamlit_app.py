from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Mr. Peach!

# Sample Input
        # 'area_home' : 140, #average area of livable space in germany
        # 'age_home' : 1960,
        # 'number_people' : 3,
        # 'age_windows' : 1980,
        # 'number_panes' : 1,
        # 'age_heating' : 1990,
        # 'old_type_heating' : 0, #oil heating
        # 'number_floor' : 2

# Sample output
        # {'window': {'funding': 20, 'renovate': 1, 'cost': 12000, 'savings': 440}, 'heating': {'funding': '50', 'renovate': 1, 'cost': '15000', 'savings': '0'}}
"""

import requests


with st.echo(code_location='below'):

    area_home = st.text_input("area_home")
    age_home = st.text_input("age_home")
    number_people = st.text_input("number_people")
    age_windows = st.text_input("age_windows")
    number_panes = st.text_input("number_panes")
    old_type_heating = st.text_input("old_type_heating")
    number_floor = st.text_input("number_floor")
    # 'area_home' : 140, #average area of livable space in germany
    # 'age_home' : 1960,
    # 'number_people' : 3,
    # 'age_windows' : 1980,
    # 'number_panes' : 1,
    # 'age_heating' : 1990,
    # 'old_type_heating' : 0, #oil heating
    # 'number_floor' : 2

    # url = 'https://interhyp-dps.ew.r.appspot.com/'
    url = 'https://mrpeach-dot-interhyp-dps.ew.r.appspot.com'
    # url = 'http://127.0.0.1:5000'

    params = {'area_home' : 140, #average area of livable space in germany
            'age_home' : 1960,
            'number_people' : 3,
            'age_windows' : 1980,
            'number_panes' : 1,
            'age_heating' : 1990,
            'old_type_heating' : 0, #oil heating
            'number_floor' : 2
            }
    response = requests.post(url, params)


    # Point = namedtuple('Point', 'x y')
    # data = []

    # points_per_turn = total_points / num_turns

    # for curr_point_num in range(total_points):
    #     curr_turn, i = divmod(curr_point_num, points_per_turn)
    #     angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    #     radius = curr_point_num / total_points
    #     x = radius * math.cos(angle)
    #     y = radius * math.sin(angle)
    #     data.append(Point(x, y))

    # st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    #     .mark_circle(color='#0068c9', opacity=0.5)
    #     .encode(x='x:Q', y='y:Q'))
