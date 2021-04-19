from psychopy import visual, core, event
import random
import pandas as pd
import datetime
import os
import re

def drawitintro(win, text, text_colour=[255, 255, 255], key='space'):
    message = visual.TextStim(win, text=text, color=text_colour)
    message.draw()
    win.flip()
    event.waitKeys(keyList=[key])


def draw_right_wrong(win, text):
    message = visual.TextStim(win, text=text, color=[255, 255, 255])
    message.draw()
    win.flip()
    core.wait(0.3)


def drawitstroop(win, text, text_colour, key):
    colour_key = ['b', 'r', 'g', 'y']
    message = visual.TextStim(win, text=text, color=text_colour)
    message.draw()
    win.flip()
    timer = core.Clock()
    pressed_key = event.waitKeys(maxWait=5, keyList=colour_key, timeStamped=timer)
    if pressed_key is not None:
        if pressed_key[0][0] != key:
            draw_right_wrong(win, "Wrong!")
        else:
            draw_right_wrong(win, "Correct!")
    return pressed_key


def stroopTest(win):
    colour_word = ["BLUE", "RED", "GREEN", "YELLOW"]
    colour_key = ['b', 'r', 'g', 'y']
    colour_codes = [[0, 0, 255], [255, 0, 0], [0, 255, 0], [255, 255, 0]]

    congruent = random.randint(0, 1)
    colour = random.randint(0, 3)

    # If congruent just write one of the 4 colours using its own colour
    if congruent:
        return drawitstroop(win, colour_word[colour], colour_codes[colour], colour_key[colour]), \
               [colour_key[colour], colour_key[colour]]

    # If not congruent write one of the 4 colours not using its own colour
    else:
        colour_incongruent = random.randint(0, 3)
        while colour == colour_incongruent:
            colour_incongruent = random.randint(0, 3)
        return drawitstroop(win, colour_word[colour_incongruent], colour_codes[colour], colour_key[colour]), \
               [colour_key[colour_incongruent], colour_key[colour]]\


def main():
    # Introduction and Instructions
    space_phrase = "\n\n\n Press [space] to continue."
    welcome_text_1 = "Welcome to the Stroop Test developed for the Psych 363 Final Project" + space_phrase
    welcome_text_2 = "In this test you will type the key that corresponds to the colour of the font" + space_phrase
    welcome_text_3 = "Type 'b' for blue\nType 'r' for red\nType 'y' for yellow\nType 'g' for green" + space_phrase
    welcome_text_4 = "Now let's do a sample test. For the test type the key that corresponds to the colour of the " \
                     "font" + space_phrase
    welcome_text_5 = "For the sample after this page we press 'r' because the colour of the font is red." + space_phrase
    welcome_text_6 = "For the sample after this page we press 'b' because the colour of the font is blue." + space_phrase
    welcome_text_7 = "Okay, we've gone over everything. Now get ready, and once you press [space] the test beings! " \
                     "We test 20 items, so it'll take about a minute or two." + space_phrase

    win = visual.Window([800, 800], color=[-1, -1, -1])
    data_frame_format = {'Word': [], 'Ink': [], 'Response Time': [], 'Correct': []}
    df = pd.DataFrame(data_frame_format)

    drawitintro(win, welcome_text_1)
    drawitintro(win, welcome_text_2)
    drawitintro(win, welcome_text_3)
    drawitintro(win, welcome_text_4)
    drawitintro(win, welcome_text_5)
    drawitintro(win, "RED", [255, 0, 0], 'r')
    drawitintro(win, welcome_text_6)
    drawitintro(win, "RED", [0, 0, 255], 'b')
    drawitintro(win, welcome_text_7)

    # Test begins here
    for i in range(20):
        timing_info = stroopTest(win)
        if timing_info[0] is None:
            continue
        pressed_key = timing_info[0][0][0]
        response_time = timing_info[0][0][1]
        ink = timing_info[1][1]
        word = timing_info[1][0]
        append_element = {'Word': word, 'Ink': ink, 'Response Time': response_time, 'Correct': pressed_key == ink}
        df = df.append(append_element, ignore_index=True)
    now = datetime.datetime.now()
    name = re.findall("home/(\w+)/", os.getcwd())
    if len(name):
        name = name[0]
    else:
        name = "StroopTest"
    file_name = '{}_stroop_{}_{}_{}_{}.csv'.format(name, now.day, now.hour, now.minute, now.second)
    df.to_csv(file_name, index=False)

if __name__ == "__main__":
    main()
