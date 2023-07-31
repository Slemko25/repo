import sqlite3

conn = sqlite3.connect('input_form.sqlite')
cur = conn.cursor()


conn.close()