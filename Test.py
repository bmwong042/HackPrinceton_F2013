#!/usr/bin/env python
import bottle
import pymongo

from pymongo import MongoClient

def main():

	# database for storing users

	db_users = connection["user_database"]
    db_users.createCollection("col_users")

    # dummy user to set fields

    db_users.col_users.insert(first_name: "first_name", last_name: "last_name" , email: "name@sample.com")

    # -------------------------------------------------------------------

    # database for storing events

	db_events = connection["event_database"]
	db_events.createCollection("col_events")

	# dummy event to set fields

	db_events.col_events.insert(event_name: "eventname", possible_times: [])

	# -------------------------------------------------------------------

    db = connection["user_database"]
    db.createCollection("users")

    db.users.insert(first_name: "fname", last_name: "lname" , email: "fl@sample.com")

