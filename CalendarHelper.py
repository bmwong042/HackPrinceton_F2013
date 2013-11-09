   # --------------------------------------------------------------------------
   # CalendarHelper.py
   #
   # Conglomeration of helper classes for the calendar event and attendee data
   # types. 
   #
   # Last edited: 11.09.2013 - 09:19:10 AM - bmwong042
   #
   # --------------------------------------------------------------------------

import datetime
import calendar
import time

class Event(object):

   # --------------------------------------------------------------------------
   # @params
   #
   # preferences: aggregation of following variables - 
   #
   # --------------------------------------------------------------------------
   # self: modifying its own fields
   #
   # 0 - id: unique int identifier for event
   # 1 - event_code: unique String event_name 
   # 2 - attendees: list - attendees objs. 
   # 3 - times: dictionary - suggested times with freq [time obj., freq]
   # 4 - suggestions: dictionary - suggested events (fixed), with freq [event,freq]
   #
   # --------------------------------------------------------------------------
   #
   # constructing a new self event object - setting all preferences
   #
   # --------------------------------------------------------------------------

   def __init__(self, event_id, event_code, attendees, times, suggestions):
      self.preferences = {id, event_code, attendees, times, suggestions}

   # ID -----------------------------------------------------------------------
   #
   # self.preferences[0] - event code (String - code)
   #
   # --------------------------------------------------------------------------

   def set_id(self, newID):
      self.preferences[0] = newID

   def get_id(self):
      return self.preferences[0]


   # event_code (name) --------------------------------------------------------
   #
   # self.preferences[1] - event code (String - code)

   def set_code(self, newCode):
      self.preferences[1] = newCode

   def get_code(self):
      return self.preferences[1]


   # attendees ----------------------------------------------------------------
   #
   # self.preferences[2] - attendees (list - objs)
   #
   # --------------------------------------------------------------------------

   def add_attendee(self, attendee_obj):
      self.preferences[2].append(attendee_obj)

   def remove_attendee(self, attendee_obj):
      self.preferences[2].remove(attendee_obj)

   def get_all_attendees(self):
      return self.preferences[2]

   def contains_attendee(self, attendee_obj):
      return self.preferences[2].count(attendee_obj) != 0


   # times --------------------------------------------------------------------
   #
   # self.preferences[3] - times (dict - [times, freq])   
   #
   # --------------------------------------------------------------------------

   def add_time(self, newTime):
      if (contains_time(self, newTime)):
         self.preferences[3][newTime] += 1
      else:
         self.preferences[3].insert(newTime, 1)

   # remove should be callable only by event owner. use check for that. 
   # TO DO. 
   def remove_time(self, time_rem):
      if (contains_time(self, time_rem)):
         del self.preferences[3][time_rem]
      else:
         return

   def get_times(self):
      return self.preferences[3]
   
   def contains_time(self, o_time):
      return self.preferences[3].count(oTime) != 0


   # suggestions --------------------------------------------------------------
   #
   # ----- can be commented out if undesired -----
   #
   # self.preferences[4] - suggestions (dict - [sugg, freq])
   #
   # following two methods are used for if the suggestions are open to all
   #
   # --------------------------------------------------------------------------

   def add_suggestion(self, str_sugg):
      if (contains_sugg(self, str_sugg)):
         self.preferences[4][str_sugg] += 1
      else:
         self.preferences[4].insert(str_sugg, 1)

   def contains_sugg(self, str_sugg):
      self.preferences[4].count(str_sugg) != 0

class Attendee(object):
   # @params
   #
   # data: aggregation of following variables - 
   #
   # --------------------------------------------------------------------------
   # self: modifying its own fields
   #
   # 0 - attendee_id: unique int identifier for each attendee
   # 1 - name: unique String name
   # 2 - attendees: list - attendees objs. 
   # 3 - available_ times: list - all times for which they are free
   # 4 - comment: String - their comment on the event
   #
   # --------------------------------------------------------------------------
   #
   # constructing a new attendee object - setting all preferences
   #
   # --------------------------------------------------------------------------

   def __init__(self, attendee_id, name, available_times, comment):
      self.information = {attendee_id, name, available_times, comment}

   # ID -----------------------------------------------------------------------
   #
   # self.information[0] - int representation of unique ID
   #
   # --------------------------------------------------------------------------

   def set_id(self, newID):
      self.information[0] = newID

   def get_id(self):
      return self.information[0]


   # name ---------------------------------------------------------------------
   #
   # self.information[1] - String representation of name
   #
   # --------------------------------------------------------------------------

   def set_name(self, str_name):
      self.information[1] = str_name

   def get_name(self):
      return self.information[1]

   # available_times ----------------------------------------------------------
   #
   # self.information[2] - avilable_times (list - time objs.)
   #
   # --------------------------------------------------------------------------

   def add_time(self, o_newTime):
      if (contains_time(self, o_newTime)):
         self.information[2].append(o_newTime)
      else:
         return

   def remove_time(self, time_rem):
      if (contains_time(self, time_rem)):
         self.information[2].remove(time_rem)
      else:
         return

   def get_times(self):
      return self.information[2]
   
   def contains_time(self, o_time):
      return self.information[2].count(o_time) != 0

   # comment ------------------------------------------------------------------
   #
   # self.information[3] - String representation of inserted comment
   #
   # --------------------------------------------------------------------------

   def set_comment(self, str_comment):
      self.information[3] = str_comment

   def get_comment(self):
      return self.information[3]
