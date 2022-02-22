#!/usr/bin/env python3
# Justin Clark
# 2022/02/22

# main.py

import tkinter as tk
import twitch_data as td

root = tk.Tk()

root.geometry("600x400")

# Show Graph
def display_graph(type):
    ''' Display a pie graph based on the string type '''
    if type == '' or  type == None:
        print("No type param passed")
        return
    elif type == 'view':
        td.graph_setup(type)
    elif type == 'follow':
        td.graph_setup(type)

streamer_limit = 0
streamer_lim_var = tk.StringVar()
streamer_lim_var.set("0")

# Labels
label_01 = tk.Label(root, text="Top Streamers")
label_01.pack()

label_foll_cap = tk.Label(root, text=streamer_lim_var.get())
label_foll_cap.pack()

def change_limit(n):
    ''' increment the streamer limit '''
    global streamer_limit
    streamer_limit += n
    streamer_lim_var.set(str(streamer_limit))

    label_foll_cap['text'] = streamer_lim_var.get(streamer_limit)

    print(streamer_lim_var.get())

# Buttons
button_01 = tk.Button(root, text="By Viewership (avg)", command= lambda: display_graph('view'))
button_01.pack()

button_02 = tk.Button(root, text="By Followers", command= lambda: display_graph('follow')).pack()
button_02.pack()

button_left = tk.Button(root, text="<", command= lambda: change_limit(-1))
button_left.pack()

button_right = tk.Button(root, text=">", command= lambda: change_limit(1)).pack()
button_right.pack()

root.mainloop()
