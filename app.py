from flask import Flask, jsonify, request, render_template
import sqlite3
import requests

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect("weather_data.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL
    );""")
    conn.commit()
    conn.close()

create_table()

def fetch_and_save_weather_data(city_name):
    api_key = '66e13fd96a3720af7e158494b56b3514'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    print(url)
    print('fetching city data...'+city_name)
    response = requests.get(url)
    data = response.json()
    print(data)
    if data.get('main') and data.get('main').get('temp') and data.get('main').get('humidity'):
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        print(temperature)
        print(humidity)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO weather_data (city_name, temperature, humidity) 
                          VALUES (?, ?, ?);""", (city_name, temperature, humidity))
        conn.commit()
        conn.close()
        return True
    else:
        return False

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    userid = request.form.get('userId')
    password = request.form.get('password')
    if userid == "admin" and password == "admin123":
        return render_template('home.html')
    else:
        return "Invalid credentials. Please try again."

@app.route('/add_city', methods=['POST'])
def add_city():
    city_name = request.get_json().get('city')
    if fetch_and_save_weather_data(city_name):
        return render_template('home.html')
    else:
        return jsonify({"message": "City not found or weather data not available"})

@app.route('/delete_city/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    print(city_id)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM weather_data WHERE id=?", (int(city_id),))
    conn.commit()
    conn.close()
    return jsonify({"message": "City deleted successfully"})

@app.route('/weather_data/<city_id>', methods=['GET'])
def get_weather_data(city_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_data WHERE id=?", (int(city_id),))
    data = cursor.fetchall()
    conn.close()
    weather_data=[]
    print(weather_data)
    
    # Return the data as JSON
    return jsonify(weather_data)

@app.route('/cities', methods=['GET'])
def get_cities():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_data")
    cities = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()
    return jsonify(cities)

if __name__ == "__main__":
    app.run(debug=True)
