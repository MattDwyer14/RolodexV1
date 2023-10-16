import json
import mysql.connector

with open('config.json', 'r') as f:
    config = json.load(f)

db = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database']
)

def fetch_entries():
    pass

def add_entry():
    pass