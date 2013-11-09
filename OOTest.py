import datetime
import calendar
import time

class Event(object)
{
	# @params
	# self: modifying its own fields
	# attendees: list - attendees for event
	# times: dictionary - suggested times with freq [time(hashed), freq]
	# suggestions: dictionary - suggested events (fixed), with freq [event, freq]

	def __init__(self, event_name, attendees, times, suggestions):
		self.data = {event_name, attendees, times, suggestions}

	# modifying event name
	# self.data[0] - event name (String - name)

	def modify_name(self, newName):
		self.data[1] = newName

	# modification of attendees
	# self.data[1] - attendees (list - names)

	def add_attendee(self, attendee_name):
		self.data[2].append(attendee_name)

	def remove_attendee(self, attendee_name):
		self.data.remove(attendee_name)

	# modification of times
	# self.data[2] - times (dict - times, freq)	

	def contains_time(self, o_time):
		for (d in self.data[2])
			return true
		return false

	def add_time(self, newTime)
		if contains_time(self, newTime):
			self.data[2][newTime]++
		else
			self.data[2].insert(newTime, 1)

	# modification of suggestions		
	# self.data[3] - suggestions (dict - sugg, freq)
}

class Date(object)
{
	
}

# to do: hash function for a date to store values

# list.insert(index, value)
# dictionary = {key : value, key : value}
# dictionary[key] - prints value mapped by key
# str(notstringthing)
# del dictionary[key] - removes that k/v pair
# import math
