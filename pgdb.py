import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import cgi
form = cgi.FieldStorage()

name = form.getvalue('name')
surname = form.getvalue('surname')
dob = form.getvalue('dob')
city = form.getvalue('city')
country = form.getvalue('country')

conn = psycopg2.connect(database="dataedo_test", user="postgres", password="gigogo25", host="127.0.0.1", port="5432")
print('Open succesfully')

cur = conn.cursor()

insert_query = sql.SQL("""
    INSERT INTO submit_form (name, surname, dob, city, country)
    VALUES (%s, %s, %s, %s, %s)
    """)
cur.execute(insert_query, (name, surname, dob, city, country))



conn.commit()
cur.close()
conn.close()

print("Content-type: text/html")
print()
print("<h1>Form submitted successfully!</h1>")
