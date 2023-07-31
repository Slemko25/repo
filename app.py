import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# PostgreSQL database configuration
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'dataedo_test'
DB_USER = 'postgres'
DB_PASSWORD = 'gigogo25'

# Create the database table
def create_table():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS form_data (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        surname TEXT,
                        dob DATE,
                        city TEXT,
                        country TEXT
                    )''')
    conn.commit()
    conn.close()

# Route for the form page
@app.route('/')
def form():
    return render_template('input_form.html')

# Route for form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    surname = request.form['surname']
    dob = request.form['dob']
    city = request.form['city']
    country = request.form['country']

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO form_data (name, surname, dob, city, country) VALUES (%s, %s, %s, %s, %s)',
                   (name, surname, dob, city, country))
    conn.commit()
    conn.close()

    return 'Form submitted successfully.'

if __name__ == '__main__':
    create_table()
    app.run()
