import datetime
import calendar
import time

class Event(object)
{
   # @params
   #
   #
   # preferences: aggregation of following variables - 
   #
   # ------------------------------------------------------------------------
   # self: modifying its own fields
   # attendees: list - attendees for event
   # times: dictionary - suggested times with freq [time(hashed), freq]
   # suggestions: dictionary - suggested events (fixed), with freq [event,freq]
   # ------------------------------------------------------------------------
   #
   # constructing a new self object - setting all preferences

   def __init__(self, event_name, attendees, times, suggesjtions):
      self.preferences = {event_name, attendees, times, suggestions}

   # names -------------------------------------------------------------------

   # self.preferences[0] - event name (String - name)

   def modify_name(self, newName):
      self.preferences[0] = newName

   # attendees ----------------------------------------------------------------

   # self.preferences[1] - attendees (list - names)

   def add_attendee(self, attendee_name):
      self.preferences[1].append(attendee_name)

   def remove_attendee(self, attendee_name):
      self.preferences.remove(attendee_name)

   # times -------------------------------------------------------------------

   # self.preferences[2] - times (dict - times, freq)   

   def contains_time(self, o_time):
      for (d in self.preferences[2])
         return true
      return false

   def add_time(self, newTime)
      if contains_time(self, newTime):
         self.preferences[2][newTime]++
      else
         self.preferences[2].insert(newTime, 1)

   # preferences --------------------------------------------------------------
     
   # self.preferences[3] - suggestions (dict - sugg, freq)


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
