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
   # --------------------------------------------------------------------------
   # self: modifying its own fields
   #
   # 0 - id: unique int identifier for event
   # 1 - event_code: unique String name for event
   # 2 - attendees: list - attendees for event
   # 3 - times: dictionary - suggested times with freq [time(hashed), freq]
   # 4 - suggestions: dictionary - suggested events (fixed), with freq [event,freq]
   # --------------------------------------------------------------------------
   #
   # constructing a new self object - setting all preferences

   def __init__(self, id, event_code, attendees, times, suggestions):
      self.preferences = {id, event_code, attendees, times, suggestions}

   # ID -----------------------------------------------------------------------

   # self.preferences[0] - event code (String - code)

   def modify_id(self, newID):
      self.preferences[0] = newID

   # code (name) --------------------------------------------------------------

   # self.preferences[1] - event code (String - code)

   def modify_code(self, newCode):
      self.preferences[1] = newCode

   # attendees ----------------------------------------------------------------

   # self.preferences[2] - attendees (list - names)

   def add_attendee(self, attendee_name):
      self.preferences[2].append(attendee_name)

   def remove_attendee(self, attendee_name):
      self.preferences.remove(attendee_name)

   # times --------------------------------------------------------------------

   # self.preferences[3] - times (dict - [times, freq])   

   def contains_time(self, o_time):
      for (d in self.preferences[3])
      {
         if (d.equals(o_time))
            return true
      }
      return false

   def add_time(self, newTime):
      if (contains_time(self, newTime)):
         self.preferences[3][newTime]++
      else
         self.preferences[3].insert(newTime, 1)

   # preferences --------------------------------------------------------------
     
   # self.preferences[4] - suggestions (dict - [sugg, freq])


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
