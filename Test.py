#!/usr/bin/env python

pip install pymongo

from pymongo import MongoClient

def main():
    
    connection = MongoClient()
    db_overall = connection["db_overall"]
    col_overall = connection["col_overall"]
    
    db_events = connection["event_database"]
    col_events = db["events"]
    
    db_users = connection["user_database"]
    col_users = db["users"]
    
    