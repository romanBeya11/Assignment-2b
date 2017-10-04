'''
Created by: Roman Beya
Created on: 29-sep-2017
Created for: ICS3U
This program calculates the height of an object in meters above the ground after a certain amount of seconds
'''

import ui

# constants
g = 9.81

def calculate_height_touch_up_inside(sender):
	# input the amount of time since the object has left the rest position
	seconds = float(view['object_height_textfield'].text)
	
	# processing what the height is
	height = 100 - 0.5 * g * seconds ** 2
	
	# outputting the height of the object in meters 
	view['output_label'].text = "After {0} seconds, the object is {1} meters above the ground!".format(seconds, height)

view = ui.load_view()
view.present('sheet')
