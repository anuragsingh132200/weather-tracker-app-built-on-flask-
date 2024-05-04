Sure, here's a basic README for your project:

```markdown
# Weather Monitoring App

This is a Flask application that monitors the weather of different cities.

## Features

- Fetches and stores weather data (temperature and humidity) for different cities.
- Provides an API to get the weather data for a city.
- Provides an API to delete a city from the monitoring list.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/anuragsingh132200/weather-tracker-app-built-on-flask-.git
```

2. Navigate to the project directory:

```bash
cd weather-tracker-app-built-on-flask-
```

3. Install the required Python packages:

```bash
pip install flask requests
```
** if you want then you can even create a venv for not disturbing versioning of the files
4. Run the Flask application:

```bash
python app.py
```

The application will start running at http://localhost:5000.

## Usage

- To add a city to the monitoring list, make a POST request to `/add_city` with the city name as JSON data.
- To get the weather data for a city, make a GET request to `/weather_data/<city_id>`.
- To delete a city from the monitoring list, make a DELETE request to `/delete_city/<city_id>`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

```

