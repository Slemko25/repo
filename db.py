import sqlite3

conn = sqlite3.connect('input_form.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS input_form')
cur.execute('CREATE TABLE input_form (name TEXT NOT NULL PRIMARY KEY, surname TEXT NOT NULL, dob TEXT NOT NULL, city TEXT NOT NULL, country TEXT NOT NULL)')

conn.close()