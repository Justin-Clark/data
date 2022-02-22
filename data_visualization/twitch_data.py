#!/usr/bin/env python3
# Justin Clark
# 2022/02/22

# twitch_data.py

import csv

import plotly.graph_objects as go

from plotly.subplots import make_subplots
import plotly

filename = './twitchdata-update.csv'

STREAMER_LIMIT = 25

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    streamers, view_counts, followers = [], [], []

    for i, row in enumerate(reader):

        if i > STREAMER_LIMIT:
            break

        try:
            view_counts.append(int(row[4]))
            streamers.append(row[0])
            followers.append(int(row[5]))
        except:
            print("View counts list: ", view_counts)
            print("Streamers list: ", streamers)
            print("Followers list: ", followers)
            pass

pop_viewership, pop_followers = [0 for i in range(len(view_counts) - 1)], [0 for i in range(len(view_counts) - 1)]

# Get the value to 'pop' out of the chart
top_v = max(view_counts)
top_f = max(followers)

pop_viewership[view_counts.index(top_v)] = 0.2
pop_followers[followers.index(top_f)] = 0.2

def graph_setup(type):

    if type == None or type == '':
        print("No type param passed")
        return

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    if type == 'view':
        fig.add_trace(go.Pie(labels=streamers, values=view_counts, name="avg viewers", pull=pop_viewership),1, 1)
        fig.update_traces(hole=0.4, hoverinfo="label+value+name")

        fig.update_layout(
                title_text="Top Streamers Early 2018",
                # Add annotations in the center of the donut pies.
                annotations = [
                    dict(text='AVG Views', x=0.19, y=0.5, font_size=20, showarrow=False),
                ])

    elif type == 'follow':
        fig.add_trace(go.Pie(labels=streamers, values=followers, name="followers", pull=pop_followers),1, 2)
        fig.update_traces(hole=0.4, hoverinfo="label+value+name")

    else:
        print("Incorrect Param(s)")
        return

    fig.update_layout(
            title_text="Top Streamers Early 2018",
            # Add annotations in the center of the donut pies.
            annotations = [
                dict(text='Followers', x=0.8, y=0.5, font_size=20, showarrow=False)
            ])


    plotly.offline.plot(fig)

graph_setup("follow")
